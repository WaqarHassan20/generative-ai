# 🚀 Pydantic: Data Validation & Settings Management

## 📌 What is Pydantic?

**Pydantic** is a Python library for data validation and settings using type annotations. It provides type-safe validation, automatic type coercion, clear error messages, and seamless JSON serialization.

**Key Benefits**: ✅ Reduce boilerplate | ✅ Type safety | ✅ Auto documentation | ✅ JSON support | ✅ Business rule validation

---

## 📚 Learning Path & File Guide

### **01_basic/** - Core Concepts

| File | Topic | Key Points |
|------|-------|-----------|
| **01_first_model.py** | BaseModel Basics | Create models with type annotations, instantiate from objects/dicts |
| **02_product_model.py** | Default Values | Required fields, optional fields with defaults |
| **03_field_example.py** | Field Configuration | Use `Field()` for constraints, descriptions, aliases |
| **04_employee_model.py** | Real-World Models | Model complex domain entities |
| **05_field_validation.py** | Custom Validation | `@field_validator`, `@model_validator` for business rules |
| **06_computed_property.py** | Computed Fields | `@computed_field` for derived/calculated values |
| **07_advance_validator.py** | Advanced Validation | Complex scenarios, chaining, context-aware validation |
| **08_nested_model.py** | Nested Models | Compose complex structures, type-safe hierarchies |
| **09_self_reference.py** | Self-Reference | Tree structures, recursive data |
| **10_adv_self_reference.py** | Advanced References | Circular dependencies, `ForwardRef` |
| **11_serial.py** | Serialization | `.model_dump()`, `.model_dump_json()`, parsing |
| **12_good_practices.md** | Best Practices | Organization, performance, patterns, error handling |

---

## 🎓 Core Concepts

**Type Annotations** → Validates based on type hints: `str`, `int`, `list`, `Union`, `Optional`  
**Validation Modes** → Before (rare) | After (common) | Wrap (custom)  
**Error Handling** → Catch `ValidationError`, access `.errors()` for details  
**Model Config** → Use `model_config = ConfigDict()` for settings  

---

## 🔧 Common Use Cases

- **API Models**: FastAPI/Flask request/response validation
- **Config Management**: Load environment variables safely  
- **Data Pipeline**: Validate before processing/storing
- **Type Safety**: Runtime type checking with clear errors

---

## 📖 Quick Reference

| Operation | Code |
|-----------|------|
| Create Model | `class User(BaseModel): id: int` |
| Create Instance | `user = User(id=1, name="John")` |
| From Dictionary | `User(**{"id": 1, "name": "John"})` |
| To Dictionary | `user.model_dump()` |
| To JSON | `user.model_dump_json()` |
| From JSON | `User.model_validate_json(json_str)` |
| Field Validation | `@field_validator("field_name")` |
| Model Validation | `@model_validator(mode='after')` |
| Field Constraints | `field: str = Field(min_length=3)` |
| Computed Field | `@computed_field @property` |

---

## 🚀 Quick Start

```python
from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    id: int
    name: str = Field(min_length=1)
    email: str
    
    @field_validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

# Usage
user = User(id=1, name="John", email="john@example.com")
print(user.model_dump_json())
```

---

## 💡 Performance Tips

✅ Prefer model references over nested objects  
✅ Limit nesting depth to 3-4 levels  
✅ Use validators sparingly  
✅ Cache validation results for batches  
✅ Profile models for bottlenecks  

---

## 🔗 Integrations

- **FastAPI** - Built-in validation & docs
- **SQLAlchemy** - ORM ↔ Pydantic models
- **Databases** - JSON serialization
- **Type Checking** - mypy, pyright support

---

**Next Steps**: Study files in order → Run examples → Experiment → Review best practices!

