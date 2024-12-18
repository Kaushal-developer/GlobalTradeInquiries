from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_type(image):
    """
    Validate uploaded file type to ensure it's an image.
    """
    valid_mime_types = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
    file_mime_type = image.file.content_type
    if file_mime_type not in valid_mime_types:
        raise ValidationError(
            _("Unsupported file type. Allowed types: JPEG, PNG, GIF, WEBP.")
        )

class Category(models.Model):
    """
    Model to represent a product category.
    """
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(
        upload_to='category/images/',
        validators=[validate_image_type],
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """
    Model to represent a product.
    """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    image = models.ImageField(
        upload_to='products/images/',
        validators=[validate_image_type],
        blank=True,
        null=True
    )
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

from django.utils import timezone

class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount = models.CharField(max_length=50)  # E.g., 20% OFF
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='offer_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def is_expired(self):
        return timezone.now() > self.end_time

    def time_left(self):
        if self.end_time > timezone.now():
            return str(self.end_time - timezone.now()).split()[0]
        return "Expired"

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Model to represent the Contact Us form / Lead Generation inquiries
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='leads',
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        related_name='product_inquiries',
        blank=True,
        null=True
    )
    inquiry_type = models.CharField(
        max_length=50,
        choices=[
            ('general', 'General Inquiry'),
            ('bulk_order', 'Bulk Order'),
            ('pricing', 'Pricing Inquiry'),
            ('product_request', 'Product Request'),
            ('custom_request', 'Custom Request'),
        ],
        default='general',
    )
    message = models.TextField(blank=True, null=True)
    preferred_contact_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.inquiry_type}"

    def is_recent(self):
        return timezone.now() - self.created_at < timezone.timedelta(days=30)

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ['-created_at']  # Most recent inquiries first
