# API Test Cases - JSONPlaceholder API

## Test Case Overview
This document contains detailed test cases for API testing using JSONPlaceholder as the test endpoint.

---

## TC-API-001: Get All Posts

**Objective:** Verify that the API returns all posts successfully

**Preconditions:** 
- API endpoint is accessible
- Internet connection available

**Test Steps:**
1. Send GET request to `/posts`
2. Verify response status code
3. Verify response structure
4. Validate data types

**Expected Results:**
- Status Code: 200
- Response: Array of post objects
- Each post contains: userId, id, title, body
- Array length > 0

**Test Data:** N/A

**Priority:** High

**Test Type:** Functional

---

## TC-API-002: Get Specific Post

**Objective:** Verify retrieval of a specific post by ID

**Preconditions:** 
- API endpoint is accessible
- Valid post ID exists

**Test Steps:**
1. Send GET request to `/posts/{id}` where id = 1
2. Verify response status code
3. Verify response structure
4. Validate returned post ID matches request

**Expected Results:**
- Status Code: 200
- Response: Single post object
- Post ID matches requested ID
- All required fields present

**Test Data:** 
- Post ID: 1

**Priority:** High

**Test Type:** Functional

---

## TC-API-003: Create New Post

**Objective:** Verify creation of a new post

**Preconditions:** 
- API endpoint is accessible
- Valid post data available

**Test Steps:**
1. Prepare post data (title, body, userId)
2. Send POST request to `/posts` with data
3. Verify response status code
4. Verify created post data matches input
5. Verify new ID is assigned

**Expected Results:**
- Status Code: 201
- Response contains new post with assigned ID
- Input data matches response data
- All fields populated correctly

**Test Data:**
```json
{
  "title": "QA Test Post",
  "body": "This is a test post created by QA automation",
  "userId": 1
}
```

**Priority:** High

**Test Type:** Functional

---

## TC-API-004: Update Existing Post

**Objective:** Verify updating an existing post

**Preconditions:** 
- API endpoint is accessible
- Valid post ID exists
- Updated post data available

**Test Steps:**
1. Prepare updated post data
2. Send PUT request to `/posts/{id}` with data
3. Verify response status code
4. Verify updated data matches input
5. Verify post ID remains unchanged

**Expected Results:**
- Status Code: 200
- Response contains updated post data
- Post ID remains the same
- Updated fields reflect new values

**Test Data:**
```json
{
  "id": 1,
  "title": "Updated QA Test Post",
  "body": "This post has been updated by QA automation",
  "userId": 1
}
```

**Priority:** High

**Test Type:** Functional

---

## TC-API-005: Delete Post

**Objective:** Verify deletion of a post

**Preconditions:** 
- API endpoint is accessible
- Valid post ID exists

**Test Steps:**
1. Send DELETE request to `/posts/{id}` where id = 1
2. Verify response status code
3. Verify response format

**Expected Results:**
- Status Code: 200
- Request processed successfully

**Test Data:** 
- Post ID: 1

**Priority:** Medium

**Test Type:** Functional

---

## TC-API-006: Get Non-Existent Post

**Objective:** Verify error handling for non-existent resource

**Preconditions:** 
- API endpoint is accessible

**Test Steps:**
1. Send GET request to `/posts/{id}` where id = 9999
2. Verify response status code
3. Verify error handling

**Expected Results:**
- Status Code: 404
- Appropriate error response

**Test Data:** 
- Post ID: 9999 (non-existent)

**Priority:** Medium

**Test Type:** Negative

---

## TC-API-007: Get All Users

**Objective:** Verify retrieval of all users

**Preconditions:** 
- API endpoint is accessible

**Test Steps:**
1. Send GET request to `/users`
2. Verify response status code
3. Verify response structure
4. Validate user data structure

**Expected Results:**
- Status Code: 200
- Response: Array of user objects
- Each user contains: id, name, username, email
- Array length > 0

**Test Data:** N/A

**Priority:** Medium

**Test Type:** Functional

---

## TC-API-008: Get Comments for Post

**Objective:** Verify retrieval of comments for a specific post

**Preconditions:** 
- API endpoint is accessible
- Valid post ID exists

**Test Steps:**
1. Send GET request to `/posts/{id}/comments` where id = 1
2. Verify response status code
3. Verify response structure
4. Validate comment data structure

**Expected Results:**
- Status Code: 200
- Response: Array of comment objects
- Each comment contains: postId, id, name, email, body
- postId matches requested post ID

**Test Data:** 
- Post ID: 1

**Priority:** Medium

**Test Type:** Functional

---

## TC-API-009: Response Time Performance

**Objective:** Verify API response time meets performance requirements

**Preconditions:** 
- API endpoint is accessible
- Stable network connection

**Test Steps:**
1. Record start time
2. Send GET request to `/posts`
3. Record end time
4. Calculate response time
5. Verify response time threshold

**Expected Results:**
- Response time < 2000ms
- Status Code: 200
- Valid response data

**Test Data:** N/A

**Priority:** Medium

**Test Type:** Performance

---

## TC-API-010: Multiple Endpoints Validation

**Objective:** Verify multiple API endpoints are accessible

**Preconditions:** 
- API endpoints are accessible

**Test Steps:**
1. Send GET requests to multiple endpoints
2. Verify each response status code
3. Verify response data types

**Expected Results:**
- Status Code: 200 for all endpoints
- Valid response format for each
- No endpoint failures

**Test Data:** 
- Endpoints: `/posts`, `/users`, `/albums`, `/todos`

**Priority:** Low

**Test Type:** Smoke

---

## Test Execution Summary

| Test Case | Priority | Type | Automation Status |
|-----------|----------|------|-------------------|
| TC-API-001 | High | Functional | ✅ Automated |
| TC-API-002 | High | Functional | ✅ Automated |
| TC-API-003 | High | Functional | ✅ Automated |
| TC-API-004 | High | Functional | ✅ Automated |
| TC-API-005 | Medium | Functional | ✅ Automated |
| TC-API-006 | Medium | Negative | ✅ Automated |
| TC-API-007 | Medium | Functional | ✅ Automated |
| TC-API-008 | Medium | Functional | ✅ Automated |
| TC-API-009 | Medium | Performance | ✅ Automated |
| TC-API-010 | Low | Smoke | ✅ Automated |

**Total Test Cases:** 10  
**Automated:** 10 (100%)  
**Coverage:** Complete API functionality
