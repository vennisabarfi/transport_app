from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ #allow internationalization
from django.contrib.auth.hashers import make_password



# User last login information 
def update_last_login(sender, user, **kwargs):
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])

# Create and save a user with the given username, email, and password.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("A name is required to create a user.")
        if not email:
            raise ValueError("Users require an email address.")
        email = self.normalize_email(email)
        username = username.strip()
        user = self.model(username=username, email=email, **extra_fields)
        user.make_password(password)
        user.save(using=self._db)
        return user
    # manage admins 
class AdminManager(BaseUserManager):
    use_in_migrations = True

    def create_admin(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("A name is required to create a user.")
        if not email:
            raise ValueError("Users require an email address.")
        email = self.normalize_email(email)
        username = username.strip()
        admin_user = self.model(username=username, email=email, **extra_fields)
        admin_user.make_password(password)
        admin_user.save(using=self._db)
        return admin_user

# admin group manager for AdminGroup model
class AdminGroupManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self,name):
        return self.get(name=name)

#Expand on this and include all permissions
class AdminPermission(models.Model):
    pass

class AdminGroup(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        AdminPermission,
        verbose_name=_("permissions"),
        blank=True,
    )
    objects = AdminGroupManager()

    class Meta:
        verbose_name =_("admin group")
        verbose_name_plural =_("admin groups")

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    username = models.CharField(
        _("username"),
        max_length = 255,
        unique=True, 
        blank=False,
        help_text=_("Required. 255 characters or fewer. Only Alphanumeric characters"),
        error_messages={
            "unique": _("A user with that username already exists."),
            "max_length":_("Username must be 255 characters or fewer."),
        },
        )

    email = models.EmailField(
        _("email"),
        max_length = 225, #change this if need be
        blank = False,
        unique = True,
        default = 'user@email.com',
        help_text= _("Email is required and must be 225 characters or fewer."),
        error_messages={
            'unique': _('Email address must be unique. Another user exists with this email address.'),
            'blank': _('Email cannot be left blank.'),
            'max_length':_('Email must be 225 characters or fewer.'),
        },
    )

    first_name  = models.CharField(
        _("first_name"),
          max_length=150, 
          null=True, 
          blank=False, 
          error_messages={
              "blank" :_("This field cannot be blank. First name is required")
          })
    last_name  = models.CharField(
        _("last_name"),
          max_length=150, 
          null=True, 
          blank=False, 
          error_messages={
              "blank" :_("This field cannot be blank. Last name is required")
              })
    location = models.CharField(max_length=255, blank=True)
    interests = models.TextField(help_text=_("Comma Separated values"))  # use this for recommendations
    bio = models.TextField()
    facebook = models.CharField(max_length=255, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    is_admin = models.BooleanField(default=False, blank=False) 
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined= models.DateTimeField(_("date joined"), default = timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "username"]

    class Meta:
        verbose_name = _("user") 
        verbose_name_plural = _("users")
        
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return self.username

class AdminProfile(models.Model):
    username = models.CharField(
        _("username"),
        max_length = 255,
        unique=True, 
        blank=False,
        help_text=_("Required. 255 characters or fewer. Only Alphanumeric characters"),
        error_messages={
            "unique": _("A user with that username already exists."),
            "max_length":_("Username must be 255 characters or fewer."),
        },
        )

    first_name  = models.CharField(
        _("first_name"),
          max_length=150, 
          null=True, 
          blank=False, 
          error_messages={
              "blank" :_("This field cannot be blank. First name is required")
          })
    last_name  = models.CharField(
        _("last_name"),
          max_length=150, 
          null=True, 
          blank=False, 
          error_messages={
              "blank" :_("This field cannot be blank. Last name is required")
              })
    location = models.CharField(max_length=255, blank=True)
    is_admin = models.BooleanField(
        default=True, 
        blank=False, 
        help_text=_("Designates that this user has all permissions" 
                    "without explicitly assigning them")) #expand on this with permissions
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined= models.DateTimeField(_("date joined"), default = timezone.now)
    objects = AdminManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ["email", "username"]

    groups = models.ManyToManyField(
        AdminGroup,
        verbose_name= _("groups"),
        blank= True,
        help_text=_(
            "This user belongs to the admin group. See group for user permissions"
        ),
        related_name = 'admin_user',
        related_query_name='admin',
    )
    # Fix this when you work on adminpermission class

    # user_permissions = models.Manager(
    #     AdminPermission,
    #     verbose_name =_("admin permissions"),
    #     blank= True, 
    #     help_text=_("Admin has all permissions."), #will specify all permissions later
    #     related_name ="admin_set",
    #     related_query_name ="admin",
    # )
    class Meta:
        verbose_name = _("user") 
        verbose_name_plural = _("users")
        
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

   
    def __str__(self):
        return self.username


