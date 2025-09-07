describe('QA Portfolio - E2E Tests', () => {
  
  beforeEach(() => {
    // Visit the base URL before each test
    cy.visit('/')
  })

  it('should load the homepage successfully', () => {
    // Verify page title
    cy.title().should('contain', 'Example Domain')
    
    // Verify main heading is visible
    cy.get('h1').should('be.visible').and('contain', 'Example Domain')
    
    // Verify page content
    cy.get('p').should('be.visible').and('contain.text', 'This domain is for use in illustrative examples')
  })

  it('should have proper page structure', () => {
    // Check for main elements
    cy.get('body').should('exist')
    cy.get('h1').should('have.length', 1)
    cy.get('p').should('have.length.at.least', 1)
    cy.get('a').should('exist')
  })

  it('should have working external link', () => {
    // Find and verify the external link
    cy.get('a[href*="iana.org"]')
      .should('be.visible')
      .and('have.attr', 'href')
      .and('contain', 'iana.org')
  })

  it('should be responsive on different viewports', () => {
    // Test desktop view
    cy.viewport(1280, 720)
    cy.get('h1').should('be.visible')
    
    // Test tablet view
    cy.viewport(768, 1024)
    cy.get('h1').should('be.visible')
    
    // Test mobile view
    cy.viewport(375, 667)
    cy.get('h1').should('be.visible')
  })

  it('should load page within acceptable time', () => {
    // Measure page load performance
    cy.window().then((win) => {
      const performanceEntries = win.performance.getEntriesByType('navigation')
      if (performanceEntries.length > 0) {
        const loadTime = performanceEntries[0].loadEventEnd - performanceEntries[0].fetchStart
        expect(loadTime).to.be.lessThan(5000) // Less than 5 seconds
      }
    })
  })
})

describe('API Integration Tests via UI', () => {
  
  it('should make API calls and verify responses', () => {
    // Test API endpoint using Cypress
    cy.request('GET', `${Cypress.env('apiUrl')}/posts/1`)
      .then((response) => {
        expect(response.status).to.eq(200)
        expect(response.body).to.have.property('id', 1)
        expect(response.body).to.have.property('title')
        expect(response.body).to.have.property('body')
        expect(response.body).to.have.property('userId')
      })
  })

  it('should handle API errors gracefully', () => {
    // Test non-existent endpoint
    cy.request({
      method: 'GET',
      url: `${Cypress.env('apiUrl')}/posts/9999`,
      failOnStatusCode: false
    }).then((response) => {
      expect(response.status).to.eq(404)
    })
  })

  it('should create new post via API', () => {
    const newPost = {
      title: 'Cypress Test Post',
      body: 'This is a test post created by Cypress',
      userId: 1
    }

    cy.request('POST', `${Cypress.env('apiUrl')}/posts`, newPost)
      .then((response) => {
        expect(response.status).to.eq(201)
        expect(response.body.title).to.eq(newPost.title)
        expect(response.body.body).to.eq(newPost.body)
        expect(response.body.userId).to.eq(newPost.userId)
        expect(response.body).to.have.property('id')
      })
  })
})

describe('Form Testing Examples', () => {
  
  beforeEach(() => {
    cy.visit('https://httpbin.org/forms/post')
  })

  it('should fill and submit form successfully', () => {
    // Fill out the form
    cy.get('input[name="custname"]').type('Cypress Test User')
    cy.get('input[name="custtel"]').type('123-456-7890')
    cy.get('input[name="custemail"]').type('cypress.test@example.com')
    
    // Select radio button
    cy.get('input[value="medium"]').check()
    
    // Select checkbox
    cy.get('input[value="pepperoni"]').check()
    
    // Fill delivery time
    cy.get('input[name="delivery"]').type('12:00')
    
    // Add comments
    cy.get('textarea[name="comments"]').type('This is a test order created by Cypress automation')
    
    // Submit form
    cy.get('input[type="submit"]').click()
    
    // Verify form submission
    cy.url().should('include', '/post')
    cy.get('pre').should('be.visible')
  })

  it('should validate required fields', () => {
    // Try to submit empty form
    cy.get('input[type="submit"]').click()
    
    // Form should still be on the same page if validation works
    cy.url().should('include', '/forms/post')
  })
})
