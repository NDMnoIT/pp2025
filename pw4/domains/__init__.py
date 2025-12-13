"""Domains package containing core classes for student management system."""

from .student import Student
from .course import Course
from .mark import Mark
from .manager import Manager

__all__ = ['Student', 'Course', 'Mark', 'Manager']
