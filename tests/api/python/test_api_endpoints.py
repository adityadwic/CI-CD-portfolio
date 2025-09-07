import pytest
import requests
import json
from jsonschema import validate


class TestJSONPlaceholderAPI:
    """
    Test suite for JSONPlaceholder API endpoints
    Demonstrates API testing best practices including:
    - Response validation
    - Status code verification
    - JSON schema validation
    - Error handling
    """
    
    base_url = "https://jsonplaceholder.typicode.com"
    
    def test_get_all_posts(self):
        """Test retrieving all posts"""
        response = requests.get(f"{self.base_url}/posts")
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0
        
        # Validate first post structure
        first_post = response.json()[0]
        required_fields = ["userId", "id", "title", "body"]
        for field in required_fields:
            assert field in first_post
    
    def test_get_specific_post(self):
        """Test retrieving a specific post by ID"""
        post_id = 1
        response = requests.get(f"{self.base_url}/posts/{post_id}")
        
        assert response.status_code == 200
        post = response.json()
        
        # Validate post structure
        assert post["id"] == post_id
        assert "userId" in post
        assert "title" in post
        assert "body" in post
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)
    
    def test_create_new_post(self):
        """Test creating a new post"""
        new_post = {
            "title": "QA Test Post",
            "body": "This is a test post created by QA automation",
            "userId": 1
        }
        
        response = requests.post(
            f"{self.base_url}/posts",
            json=new_post,
            headers={"Content-Type": "application/json"}
        )
        
        assert response.status_code == 201
        created_post = response.json()
        
        # Validate created post
        assert created_post["title"] == new_post["title"]
        assert created_post["body"] == new_post["body"]
        assert created_post["userId"] == new_post["userId"]
        assert "id" in created_post
    
    def test_update_post(self):
        """Test updating an existing post"""
        post_id = 1
        updated_data = {
            "id": post_id,
            "title": "Updated QA Test Post",
            "body": "This post has been updated by QA automation",
            "userId": 1
        }
        
        response = requests.put(
            f"{self.base_url}/posts/{post_id}",
            json=updated_data,
            headers={"Content-Type": "application/json"}
        )
        
        assert response.status_code == 200
        updated_post = response.json()
        
        assert updated_post["title"] == updated_data["title"]
        assert updated_post["body"] == updated_data["body"]
    
    def test_delete_post(self):
        """Test deleting a post"""
        post_id = 1
        response = requests.delete(f"{self.base_url}/posts/{post_id}")
        
        assert response.status_code == 200
    
    def test_get_nonexistent_post(self):
        """Test error handling for non-existent post"""
        response = requests.get(f"{self.base_url}/posts/9999")
        
        assert response.status_code == 404
    
    def test_get_users(self):
        """Test retrieving all users"""
        response = requests.get(f"{self.base_url}/users")
        
        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0
        
        # Validate user structure
        first_user = users[0]
        required_fields = ["id", "name", "username", "email"]
        for field in required_fields:
            assert field in first_user
    
    def test_get_comments_for_post(self):
        """Test retrieving comments for a specific post"""
        post_id = 1
        response = requests.get(f"{self.base_url}/posts/{post_id}/comments")
        
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)
        
        if len(comments) > 0:
            first_comment = comments[0]
            required_fields = ["postId", "id", "name", "email", "body"]
            for field in required_fields:
                assert field in first_comment
    
    def test_response_time_performance(self):
        """Test API response time performance"""
        import time
        
        start_time = time.time()
        response = requests.get(f"{self.base_url}/posts")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        assert response.status_code == 200
        assert response_time < 2.0  # Response should be under 2 seconds
    
    @pytest.mark.parametrize("endpoint", [
        "/posts",
        "/users",
        "/albums",
        "/todos"
    ])
    def test_multiple_endpoints_status(self, endpoint):
        """Test multiple endpoints for basic connectivity"""
        response = requests.get(f"{self.base_url}{endpoint}")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
