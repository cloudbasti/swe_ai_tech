# Cursor Rule Examples for Different Programming Languages

This document contains examples of Cursor rules for different programming languages and frameworks, sourced from [cursor.directory/rules/testing](https://cursor.directory/rules/testing). These rules serve as templates and examples for how to structure and write code in Cursor.

Note: This is not a general testing guide, but rather a collection of Cursor-specific rule examples that can be used as templates when working with different programming languages in Cursor.

## General Testing Principles

1. Write descriptive and meaningful test names that clearly describe the expected behavior
2. Keep tests DRY (Don't Repeat Yourself) by extracting reusable logic
3. Ensure test independence - no shared state between tests
4. Focus on critical user paths and real user behavior
5. Maintain comprehensive coverage of both typical and edge cases

## Language-Specific Testing Guidelines

### Python Testing
- Use pytest as the primary testing framework
- Write unit tests using table-driven patterns
- Separate fast unit tests from slower integration tests
- Ensure test coverage for every exported function
- Use fixtures for test setup and teardown
- Example structure:
  ```python
  def test_function_name():
      # Arrange
      test_input = [1, 2, 3]
      expected = 2
      
      # Act
      result = calculate_average(test_input)
      
      # Assert
      assert result == expected
  ```

### JavaScript/TypeScript Testing
- Use Jest for unit testing
- Use Playwright for end-to-end testing
- Utilize test fixtures for setup and teardown
- Avoid hardcoded timeouts
- Use built-in assertions and matchers
- Example structure:
  ```javascript
  describe('Function Name', () => {
    test('should do something specific', () => {
      // Arrange
      const input = [1, 2, 3];
      const expected = 2;
      
      // Act
      const result = calculateAverage(input);
      
      // Assert
      expect(result).toBe(expected);
    });
  });
  ```

### Playwright E2E Testing Best Practices
1. Use recommended built-in locators:
   - `page.getByRole`
   - `page.getByLabel`
   - `page.getByText`
   - `page.getByTitle`
2. Use `data-testid` attributes with `page.getByTestId`
3. Implement proper error handling and logging
4. Use projects for multiple browsers/devices
5. Prefer web-first assertions

### RSpec Testing (Ruby)
1. Structure:
   - Use descriptive `describe` and `context` blocks
   - Use `subject` for test objects
   - Mirror file paths in spec directory
2. Test Data:
   - Use `let` and `let!` for setup
   - Prefer factories over fixtures
3. Independence:
   - Ensure test isolation
   - Use mocks and stubs appropriately
4. Organization:
   - Group related tests logically
   - Use shared examples for common behaviors

## Testing Tools and Frameworks

### Popular Testing Frameworks
- Python: pytest, unittest
- JavaScript: Jest, Mocha
- TypeScript: Jest, Jasmine
- Ruby: RSpec
- E2E Testing: Playwright, Cypress

### Code Coverage Tools
- Python: pytest-cov
- JavaScript: Jest coverage
- Ruby: SimpleCov

## Best Practices for Test Organization

1. File Structure:
   ```
   project/
   ├── src/
   │   └── module.js
   ├── tests/
   │   ├── unit/
   │   ├── integration/
   │   └── e2e/
   └── package.json
   ```

2. Naming Conventions:
   - Unit tests: `module.test.js` or `module_test.py`
   - Integration tests: `module.integration.test.js`
   - E2E tests: `feature.spec.js`

3. Test Categories:
   - Unit Tests: Test individual components
   - Integration Tests: Test component interactions
   - E2E Tests: Test complete user flows

## CI/CD Integration

1. Run tests automatically on:
   - Pull requests
   - Merges to main branches
   - Deployments

2. Configure test reporting:
   - Generate coverage reports
   - Track test metrics
   - Set minimum coverage thresholds

## Documentation

1. Test Documentation:
   - Document test setup requirements
   - Explain test data generation
   - Document mocking strategies

2. Maintenance:
   - Regular test suite cleanup
   - Update tests with code changes
   - Review and optimize slow tests 