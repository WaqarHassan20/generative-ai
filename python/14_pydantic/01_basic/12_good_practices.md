# Pydantic Best Practices & Guidelines

## 📋 Model Organization

### Leaf Models First
- Define simple, independent models before complex ones
- Models without dependencies should be created first
- Build upward from simple to complex structures
- Example: Define `Address` model before `User` model that uses it

### Build Upward Strategy
- Start with atomic models (single responsibility)
- Compose larger models from smaller ones
- Avoid circular dependencies
- Creates a clear hierarchy and improves maintainability

### Clear & Meaningful Naming
- Use **PascalCase** for class names: `UserProfile`, `OrderItem`
- Use **snake_case** for field names: `user_id`, `created_at`
- Use descriptive names that reflect domain concepts
- Avoid vague names like `data`, `info`, `value`

### Group Related Models
- Organize in separate modules by domain/context
- Example: `models/user.py`, `models/product.py`, `models/order.py`
- Keep related configurations and validators together
- Improves code organization and maintainability

---

## ⚡ Performance Considerations

### Deep Nesting Impact
- **Problem**: Each nesting level adds validation overhead
- **Solution**: Flatten models when possible
- **Example**: Use IDs for relationships instead of full nested objects
- Keep nesting to 3-4 levels maximum for optimal performance

### Large Lists of Nested Models
- Processing large lists with nested models is expensive
- Consider pagination for large datasets
- Use generators or lazy loading for memory efficiency
- Profile performance with `pydantic.profile` if needed

### Circular References
- **Problem**: Model A references Model B, Model B references Model A
- **Solution**: Use `ForwardRef` or string annotations
- Alternative: Refactor to eliminate circular dependency
- Use `model_rebuild()` method when needed

### Lazy Loading Strategies
- Load nested data only when required
- Use properties with `@computed_field` for on-demand computation
- Consider separating read and write models
- Cache expensive operations appropriately

---

## 🎯 Data Modeling Tips

### Model Real-World Relationships
- Reflect actual business domain in your models
- Use appropriate relationship patterns:
  - **One-to-One**: Single related object
  - **One-to-Many**: List of related objects
  - **Many-to-Many**: Use junction models or lists
- Example: `User` has many `Orders`, each `Order` has many `Items`

### Use Optional Fields Appropriately
- Mark truly optional fields with `Optional[Type] = None`
- Don't over-use `Optional` - it reduces type safety
- Distinguish between:
  - **Required**: Critical business data
  - **Optional**: Nice-to-have supplementary data
  - **Nullable**: Field can be explicitly set to None
- Example: `email: str` (required) vs `phone: Optional[str] = None`

### Consider Union Types
- Use `Union[Type1, Type2]` for multiple acceptable types
- Useful for flexible data validation
- Example: `identifier: Union[str, int]` for user ID or username
- More specific than `Any` while maintaining flexibility
- Python 3.10+: Use `Type1 | Type2` syntax

### Validate Business Rules
- Use validators for complex validation logic
- Implement at the appropriate level:
  - **Field validators**: Single field validation
  - **Model validators**: Cross-field validation and business rules
- Example: Ensure `end_date > start_date`, `price > 0`
- Keep validation logic readable and well-documented

---

## 🔒 Additional Best Practices

### Field Constraints & Configuration
- Use `Field()` for detailed configuration
- Set constraints: `min_length`, `max_length`, `ge`, `le`, etc.
- Add descriptions for API documentation
- Example: `price: float = Field(gt=0, description="Product price must be positive")`

### Configuration Management
- Use `model_config` for model-wide settings
- Manage validation behavior: `validate_assignment`, `validate_default`
- Control serialization: `ser_json_timedelta`, `ser_json_bytes`
- Example: `model_config = ConfigDict(validate_assignment=True)`

### Custom Validators
- Use `@field_validator` for field-specific validation
- Use `@model_validator(mode='after')` for post-init validation
- Keep validators focused and single-responsibility
- Return modified/validated value or raise `ValueError`

### Documentation & Type Hints
- Always provide type hints - never use `Any` unless necessary
- Add docstrings to model classes
- Use field descriptions in `Field()` for automatic docs
- Improves IDE support and generates OpenAPI/Swagger docs

### Serialization Best Practices
- Choose appropriate serialization modes: `python`, `json`
- Use `alias` for different field names in JSON vs Python
- Control output with `exclude`, `include` parameters
- Use `exclude_unset` to only return explicitly set fields

### Error Handling
- Catch `ValidationError` and handle gracefully
- Extract specific error information for user feedback
- Log validation errors for debugging
- Return user-friendly error messages