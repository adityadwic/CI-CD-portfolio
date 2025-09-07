// Custom Cypress commands for reusable test actions

// Command to login (example for future use)
Cypress.Commands.add('login', (username, password) => {
  cy.visit('/login')
  cy.get('[data-cy=username]').type(username)
  cy.get('[data-cy=password]').type(password)
  cy.get('[data-cy=submit]').click()
})

// Command to check API response
Cypress.Commands.add('checkApiResponse', (endpoint, expectedStatus = 200) => {
  cy.request(endpoint).then((response) => {
    expect(response.status).to.eq(expectedStatus)
  })
})

// Command to wait for page load
Cypress.Commands.add('waitForPageLoad', () => {
  cy.window().its('document.readyState').should('equal', 'complete')
})

// Command to check element visibility with timeout
Cypress.Commands.add('shouldBeVisibleWithin', { prevSubject: true }, (element, timeout = 10000) => {
  cy.wrap(element, { timeout }).should('be.visible')
})

// Command to clear and type
Cypress.Commands.add('clearAndType', { prevSubject: true }, (element, text) => {
  cy.wrap(element).clear().type(text)
})
