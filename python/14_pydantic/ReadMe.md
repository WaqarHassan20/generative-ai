# 🚀 Pydantic: Data Validation & Settings Management

## 📌 What is Pydantic?

**Pydantic** is a powerful Python library for data validation and settings management using Python type annotations. It provides:

- **Type-safe data validation** using Python's typing system
- **Automatic type coercion** and conversion
- **Clear error messages** for validation failures
- **JSON serialization/deserialization** out of the box
- **Performance optimization** through C extension support
- **Seamless integration** with FastAPI and other frameworks

### Key Benefits
✅ Reduce boilerplate validation code  
✅ Catch data errors early with strong typing  
✅ Generate API documentation automatically  
✅ Serialize/deserialize complex nested structures  
✅ Validate business rules and constraints  
✅ Type hints everywhere for IDE support  

---

## 📚 Learning Path & Folder Structure

### **01_basic/** - Core Concepts & Fundamentals

#### 1️⃣ **01_first_model.py** - Getting Started with BaseModel
- Creating your first Pydantic model using `BaseModel`
- Defining fields with type annotations
- Instantiating models from objects and dictionaries
- Basic data validation and error handling
- **Key Concept**: `BaseModel` is the foundation of all Pydantic models

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

user = User(id=1, name="Paul", is_active=True)
```

---

#### 2️⃣ **02_product_model.py** - Model Fields & Default Values
- Adding default values to fields
- Required vs optional fields
- Model representation and printing
- Creating multiple instances with different data
- **Key Concept**: Control which fields are required and which have defaults

```python
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # Default value
```

---

#### 3️⃣ **03_field_example.py** - Advanced Field Configuration
- Using `Field()` for detailed field configuration
- Setting constraints (min_length, max_length, ge, le, etc.)
- Adding descriptions for documentation
- Custom aliases for serialization
- **Key Concept**: `Field()` provides fine-grained control over field behavior

---

#### 4️⃣ **04_employee_model.py** - Building Real-World Models
- Modeling complex domain entities (Employees)
- Handling relationships and references
- Practical real-world data structure design
- Multiple field types and configurations
- **Key Concept**: Apply Pydantic to real-world business entities

---

#### 5️⃣ **05_field_validation.py** - Data Validation
- Using `@field_validator` for field-level validation
- Using `@model_validator` for cross-field validation
- Writing custom validation logic
- Raising validation errors with meaningful messages
- **Key Concept**: Ensure data integrity through comprehensive validation

```python
from pydantic import BaseModel, field_validator

@field_validator("username")
def validate_username(cls, value):
    if len(value) < 3:
        raise ValueError("Username must be at least 3 characters")
    return value
```

---

#### 6️⃣ **06_computed_property.py** - Computed Fields
- Creating computed/derived fields using `@computed_field`
- Fields that calculate values based on other fields
- Keeping computation logic separate from data storage
- Performance implications of computed fields
- **Key Concept**: Dynamically calculate values without storing them

---

#### 7️⃣ **07_advance_validator.py** - Advanced Validation Techniques
- Complex validation scenarios
- Pre and post-initialization validation modes
- Chaining multiple validators
- Context-aware validation
- Error aggregation and reporting
- **Key Concept**: Handle sophisticated validation requirements

---

#### 8️⃣ **08_nested_model.py** - Nested Models
- Creating hierarchical data structures
- Nesting models within models
- Type-safe nested object validation
- Serialization of nested structures
- **Key Concept**: Compose complex models from simpler ones

```python
class Address(BaseModel):
    street: str
    city: str

class User(BaseModel):
    name: str
    address: Address  # Nested model
```

---

#### 9️⃣ **09_self_reference.py** - Self-Referencing Models
- Models that reference themselves
- Building tree-like structures
- Using string annotations for forward references
- Recursive data structures
- **Key Concept**: Create hierarchical self-similar data structures

---

#### 🔟 **10_adv_self_reference.py** - Advanced Self-References
- Complex self-referencing patterns
- Mutual references between models
- Using `ForwardRef` for circular dependencies
- Rebuilding models after definition
- **Key Concept**: Handle complex relationship patterns

---

#### 1️⃣1️⃣ **11_serial.py** - Serialization & Deserialization
- Converting models to JSON and dictionaries
- Using `.model_dump()` and `.model_dump_json()`
- Controlling output format with parameters
- Custom serializers for special types
- Excluding, including, and filtering fields in output
- **Key Concept**: Seamlessly convert between Python objects and JSON

```python
user = User(id=1, name="Paul", is_active=True)
user.model_dump()       # → dict
user.model_dump_json()  # → JSON string
User.model_validate_json(json_str)  # Parse from JSON
```

---

#### 1️⃣2️⃣ **12_good_practices.md** - Best Practices & Guidelines
- **Model Organization**: Structure and hierarchy
- **Performance Considerations**: Optimization strategies
- **Data Modeling Tips**: Domain-driven design
- **Field Constraints**: Validation and constraints
- **Configuration Management**: Model-wide settings
- **Serialization Best Practices**: Output formatting
- **Error Handling**: Graceful error management

---

## 🎓 Core Pydantic Concepts

### Type Annotations
- Pydantic validates based on Python type hints
- Supports all standard types: `str`, `int`, `float`, `bool`, `list`, `dict`, `set`, `tuple`
- Custom types and complex types: `Union`, `Optional`, `Literal`, `Annotated`
- Python 3.10+ union syntax: `Type1 | Type2`

### Validation Modes
- **Before**: Validate before type coercion (rare)
- **After**: Validate after type coercion (most common)
- **Wrap**: Custom validation wrapping existing validators

### Model Configuration
```python
from pydantic import ConfigDict

class User(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,      # Validate when setting attributes
        validate_default=True,         # Validate default values
        str_strip_whitespace=True,     # Strip whitespace from strings
    )
```

### Error Handling
```python
from pydantic import ValidationError

try:
    user = User(id="invalid", name="John")
except ValidationError as e:
    print(e.errors())  # List of validation errors
    print(e.json())    # JSON format errors
```

---

## 🔄 Common Patterns

### 1. **API Request/Response Models**
```python
class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
```

### 2. **Configuration Management**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False
```

### 3. **Data Validation Pipeline**
```python
# Raw data → Pydantic validation → Business logic → Database
raw_data = {"id": "123", "name": "John"}
validated_user = User(**raw_data)
save_to_database(validated_user)
```

### 4. **Field Dependencies**
```python
@model_validator(mode='after')
def validate_dates(self):
    if self.start_date > self.end_date:
        raise ValueError("Start date must be before end date")
    return self
```

---

## 💡 Performance Tips

✅ **Prefer model references** over nested objects for relationships  
✅ **Limit nesting depth** to 3-4 levels  
✅ **Use validators sparingly** - validation adds overhead  
✅ **Cache validation** results when processing batches  
✅ **Profile your models** for bottlenecks  

---

## 🔗 Integration Points

- **FastAPI**: Built-in Pydantic integration for validation and documentation
- **SQLAlchemy**: ORM models ↔ Pydantic models
- **Databases**: JSON serialization for API responses
- **Configuration**: Environment variables and dotenv files
- **Type Checking**: mypy, pyright for static analysis

---

## 📖 Quick Reference

| Task | Code |
|------|------|
| Create model | `class User(BaseModel): id: int` |
| Instantiate | `user = User(id=1, name="John")` |
| From dict | `User(**{"id": 1, "name": "John"})` |
| To dict | `user.model_dump()` |
| To JSON | `user.model_dump_json()` |
| From JSON | `User.model_validate_json(json_str)` |
| Validate field | `@field_validator("field_name")` |
| Validate model | `@model_validator(mode='after')` |
| Custom field | `field: str = Field(min_length=3)` |
| Computed field | `@computed_field @property def x(self): ...` |
| Config | `model_config = ConfigDict(...)` |

---

## 🚀 Getting Started

1. **Install Pydantic**
   ```bash
   pip install pydantic
   ```

2. **Create your first model** - See `01_first_model.py`

3. **Add validation** - See `05_field_validation.py`

4. **Build nested structures** - See `08_nested_model.py`

5. **Follow best practices** - See `12_good_practices.md`

---

## ✨ Summary

This folder covers the **complete journey** from basic model creation to advanced validation patterns. Pydantic makes your Python applications more robust by ensuring data integrity at the boundaries (APIs, databases, configuration). By understanding these concepts and following the learning path, you'll write safer, more maintainable Python code.

**Next Steps**: Study each file in order, run the examples, and experiment with your own models!
