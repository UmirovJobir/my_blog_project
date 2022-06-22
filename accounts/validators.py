from rest_framework.serializers import ValidationError

class LessThanValidator:
    def __init__(self, base):
        self.base = base
    
    def __call__(self, value):
        if len(value) < self.base:
            raise ValidationError({'error': f"Username must be greater or equal than {self.base} symbols"})


class GreaterThanValidator:
    def __init__(self, base):
        self.base = base
    
    def __call__(self, value):
        if len(value) > self.base:
            raise ValidationError({'error': f"Username must be less or equal than {self.base} symbols"})

 