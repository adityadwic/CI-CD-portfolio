#!/bin/bash

# QA Portfolio - Local Test Runner
# This script helps run all tests locally for development and validation

echo "🚀 QA Portfolio - Test Runner"
echo "=============================="

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
check_python() {
    if command -v python3 &> /dev/null; then
        print_success "Python 3 is installed"
        python3 --version
    else
        print_error "Python 3 is not installed. Please install Python 3.8+"
        exit 1
    fi
}

# Check if Node.js is installed
check_node() {
    if command -v node &> /dev/null; then
        print_success "Node.js is installed"
        node --version
    else
        print_error "Node.js is not installed. Please install Node.js 16+"
        exit 1
    fi
}

# Install Python dependencies
install_python_deps() {
    print_status "Installing Python dependencies for API tests..."
    cd tests/api/python
    
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip install -r requirements.txt
    cd ../../..
    print_success "Python dependencies installed"
}

# Install Selenium dependencies
install_selenium_deps() {
    print_status "Installing Selenium dependencies..."
    cd tests/ui/selenium
    
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip install -r requirements.txt
    cd ../../..
    print_success "Selenium dependencies installed"
}

# Install Cypress dependencies
install_cypress_deps() {
    print_status "Installing Cypress dependencies..."
    cd tests/ui/cypress
    npm install
    cd ../../..
    print_success "Cypress dependencies installed"
}

# Run API tests
run_api_tests() {
    print_status "Running API tests..."
    cd tests/api/python
    source venv/bin/activate
    
    # Create reports directory if it doesn't exist
    mkdir -p ../reports
    
    python -m pytest --junitxml=../reports/api-test-results.xml --html=../reports/api-report.html --self-contained-html
    
    if [ $? -eq 0 ]; then
        print_success "API tests completed successfully"
    else
        print_error "API tests failed"
    fi
    
    cd ../../..
}

# Run Selenium tests
run_selenium_tests() {
    print_status "Running Selenium UI tests..."
    cd tests/ui/selenium
    source venv/bin/activate
    
    # Create reports directory if it doesn't exist
    mkdir -p ../../reports
    
    python -m pytest --junitxml=../../reports/selenium-test-results.xml --html=../../reports/selenium-report.html --self-contained-html
    
    if [ $? -eq 0 ]; then
        print_success "Selenium tests completed successfully"
    else
        print_error "Selenium tests failed"
    fi
    
    cd ../../..
}

# Run Cypress tests
run_cypress_tests() {
    print_status "Running Cypress E2E tests..."
    cd tests/ui/cypress
    
    # Create reports directory if it doesn't exist
    mkdir -p ../../reports
    
    npx cypress run --reporter junit --reporter-options mochaFile=../../reports/cypress-test-results.xml
    
    if [ $? -eq 0 ]; then
        print_success "Cypress tests completed successfully"
    else
        print_error "Cypress tests failed"
    fi
    
    cd ../../..
}

# Generate test report summary
generate_summary() {
    print_status "Generating test summary..."
    
    echo ""
    echo "📊 Test Execution Summary"
    echo "========================="
    
    # Check if test result files exist and show status
    if [ -f "tests/reports/api-test-results.xml" ]; then
        print_success "✅ API Tests - Results available"
    else
        print_warning "⚠️  API Tests - No results found"
    fi
    
    if [ -f "tests/reports/selenium-test-results.xml" ]; then
        print_success "✅ Selenium Tests - Results available"
    else
        print_warning "⚠️  Selenium Tests - No results found"
    fi
    
    if [ -f "tests/reports/cypress-test-results.xml" ]; then
        print_success "✅ Cypress Tests - Results available"
    else
        print_warning "⚠️  Cypress Tests - No results found"
    fi
    
    echo ""
    print_status "Test reports are available in: tests/reports/"
    print_status "Open HTML reports in your browser to view detailed results"
}

# Main execution function
main() {
    echo ""
    print_status "Starting QA Portfolio test execution..."
    echo ""
    
    # Check prerequisites
    check_python
    check_node
    
    echo ""
    
    # Install dependencies
    install_python_deps
    install_selenium_deps
    install_cypress_deps
    
    echo ""
    
    # Create reports directory
    mkdir -p tests/reports
    
    # Run tests based on arguments
    case "${1:-all}" in
        "api")
            run_api_tests
            ;;
        "selenium")
            run_selenium_tests
            ;;
        "cypress")
            run_cypress_tests
            ;;
        "ui")
            run_selenium_tests
            run_cypress_tests
            ;;
        "all")
            run_api_tests
            run_selenium_tests
            run_cypress_tests
            ;;
        "setup")
            print_success "Setup completed! Dependencies installed."
            ;;
        *)
            echo "Usage: $0 [api|selenium|cypress|ui|all|setup]"
            echo ""
            echo "Options:"
            echo "  api      - Run only API tests"
            echo "  selenium - Run only Selenium UI tests"
            echo "  cypress  - Run only Cypress E2E tests"
            echo "  ui       - Run both Selenium and Cypress tests"
            echo "  all      - Run all tests (default)"
            echo "  setup    - Only install dependencies"
            exit 1
            ;;
    esac
    
    echo ""
    generate_summary
    echo ""
    print_success "Test execution completed! 🎉"
}

# Run main function with all arguments
main "$@"
