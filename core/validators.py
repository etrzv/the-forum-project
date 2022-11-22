from django.core.exceptions import ValidationError


def validate_only_letters(name):
    if not all([ch.isalpha() for ch in name]):
        raise ValidationError('The name should consist only of alphabetic characters.')
    return None


def validate_file_max_size_in_mb(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {max_size}MB')
    return validate

