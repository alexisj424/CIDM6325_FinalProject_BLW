# Part B — Application Architecture Critique

## Introduction
Django’s app structure promotes modularity, maintainability, and separation of concerns. This critique evaluates the strengths and limitations of Django’s architecture, referencing Layman’s *Understand Django*, Chapters 7–8.

## Strengths
- Clear separation between models, views, and templates.
- Reusable apps through pluggable architecture.
- Strong conventions reduce cognitive overhead.
- CBVs enable powerful inheritance and reusable patterns.

## Limitations
- Overuse of “magic” in CBVs can hide logic.
- Tight coupling between views and ORM.
- App boundaries can become blurry in large systems.
- Harder to test when business logic lives in views.

## Opportunities for Modularization
- Introduce services layer for business logic.
- Add mixins for permissions, logging, and validation.
- Use ADRs for architectural decisions.
- Adopt fat-model or service-first patterns for scaling.

## Conclusion
Django apps are clean and scalable when structured correctly, but require intentional design to avoid bloated views and tangled logic. Our project moves toward best practices with CBVs, mixins, and modular code organization.
