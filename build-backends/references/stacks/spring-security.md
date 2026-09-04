# Spring Security

Use this reference when a Spring-based project uses Spring Security or when a requested Java feature crosses
authentication, authorization, session, CSRF, OAuth/OIDC, or another Spring Security boundary.

Official source: https://docs.spring.io/spring-security/reference/

This reference supplements `secure-boundaries`; it does not replace the trust-boundary workflow for
high-impact changes.

## Preserve the configured security model

Inspect:

- Servlet vs reactive security.
- Session-based vs token/bearer authentication.
- Security filter chain(s) and matcher ordering.
- Method security.
- Password encoding and credential lifecycle.
- CSRF/CORS configuration.
- OAuth2/OIDC resource server/client/authorization-server relationships if present.
- Custom authentication providers, filters, converters, handlers, and access-denied behavior.

Do not add a second authentication model alongside an existing one without a migration need.

## Authorization

- Enforce authorization at the server-side protected action.
- Keep resource ownership and tenant checks explicit; URL matching alone is not object authorization.
- Treat method-security annotations and filter rules as complementary boundaries.
- Test anonymous, wrong-user, wrong-role, cross-tenant, invalid/expired credential, and allowed cases where relevant.

## Sessions and tokens

- Do not log raw credentials, bearer tokens, refresh tokens, session identifiers, or security contexts.
- Preserve issuer, audience, expiry, signature, key-rotation, and revocation assumptions.
- Avoid home-grown JWT parsing/validation when configured Spring Security support already owns it.
- Do not disable CSRF simply to make a failing browser request pass; first identify the authentication/session model.

## Error behavior

Keep unauthenticated and unauthorized outcomes distinct when the public contract requires it, while avoiding
resource enumeration or cross-tenant leakage.
