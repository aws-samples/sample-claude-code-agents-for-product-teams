# generated API docs

_Produced by: Inline / API code documentation_

**Business outcome supported:** produce working, tested, instrumented increments that meet the Definition of Done, with stakeholder-accepted quality and documented lessons for continuous improvement.

**Primary owner:** Developer

**Stakeholders:** _(none listed)_

**Accelerated MVP:** slim when the API surface is small — generated docs on the endpoints that exist

## What this is

Machine-generated API reference — OpenAPI/Swagger, GraphQL schema, protobuf docs, or equivalent — plus the inline code documentation it derives from. Updated automatically with code changes so drift is impossible.

## Why it matters for the Developer

API docs are the contract you publish to every future consumer — internal teams, partners, your own future selves. Generating them from the code guarantees they match reality and reduces the "I'll update the docs later" debt that makes APIs unusable within two quarters.

## Definition of Done

- [ ] Every published endpoint or operation has a generated reference entry
- [ ] Request and response schemas include examples
- [ ] Auth requirements and error model are documented
- [ ] Versioning and deprecation markers are present where applicable
- [ ] The build artifact is published to the docs portal per commit

## What it contains

- Generated reference for all published endpoints / operations
- Request/response schemas with examples
- Auth requirements and error model
- Versioning and deprecation markers
- Example payloads and error cases
- Build artifact published to docs portal per commit

## Inputs you rely on

- API specification (design-time source of truth)
- Feature code with doc-comments
- Docs toolchain in the CI pipeline
- Style conventions (naming, example formats)
- API governance rules

## Who consumes it

- Consumers of the API (internal and external developers)
- Technical Writer — layers narrative docs on top of the reference
- QA/Tester — uses generated schemas for contract and fuzz tests
- Sales & Marketing — uses API surface in battlecards for technical buyers

## Common pitfalls

- Generator runs but output isn't published anywhere useful
- Doc-comments minimal — schemas generated but unreadable
- Examples absent or wrong — consumers reverse-engineer from traffic
- Versioning unclear — clients can't tell which spec matches which runtime
