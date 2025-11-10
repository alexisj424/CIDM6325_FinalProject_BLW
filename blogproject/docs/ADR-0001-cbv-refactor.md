# ADR 0001: Refactor from Function-Based Views (FBVs) to Class-Based Views (CBVs)

## Context
The project originally used Function-Based Views for all CRUD operations related to posts. While FBVs are simple and explicit, they become harder to maintain and scale as complexity grows. Django’s Class-Based Views offer better modularity, reusability, and consistency.

## Decision
We refactored the Post CRUD system to use:
- PostListView
- PostDetailView
- PostCreateView
- PostUpdateView
- PostDeleteView

These leverage inheritance, mixins, and Django’s generic views.

## Rationale
- CBVs eliminate repetitive code.
- Mixins improve permission handling (LoginRequiredMixin, AuthorRequiredMixin).
- Generic views reduce boilerplate.
- Improved scalability using modular override methods (get_queryset, form_valid, get_context_data).

## Consequences
- Codebase is now more maintainable.
- Easier to extend features (pagination, filters, HTMX).
- Requires team familiarity with CBV architecture.
