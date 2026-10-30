# Entity-relationship diagram

Update this file in the same pull request as any model change.

## Implemented: account app

```mermaid
erDiagram
    USER ||--|| PROFILE : has
    PROFILE ||--o{ ADDRESS : has
    USER }o--o{ GROUP : member_of
    USER }o--o{ PERMISSION : granted
    GROUP }o--o{ PERMISSION : includes

    USER {
        bigint id PK
        string email UK "login identifier"
        string password "hashed"
        datetime last_login
        int type "UserType choices, default customer"
        bool is_staff
        bool is_superuser
        bool is_active "false means disabled"
        bool is_verified "true means email confirmed"
        datetime created_date
        datetime updated_date
    }

    PROFILE {
        bigint id PK
        bigint user_id FK, UK "one to one with user"
        string first_name "optional"
        string last_name "optional"
        string image "optional, profile_pics"
        text bio "optional"
        datetime created_date
        datetime updated_date
    }

    ADDRESS {
        bigint id PK
        bigint profile_id FK
        string title "Home, Work"
        string recipient_name
        string phone_number
        string country
        string state "optional"
        string city
        string street_address
        string postal_code "optional"
        bool is_default "one true per profile"
        datetime created_date
        datetime updated_date
    }
```

### Notes

- A **Profile** is created automatically for every new user, by a `post_save` signal.
- **Address** has a conditional unique constraint, `one_default_address_per_profile`: each profile may have many addresses, but only one with `is_default = true`.
- `created_date` and `updated_date` on Profile and Address come from the abstract `TimeStampedModel` in `core`. It creates no table of its own.
- `password` and `last_login` come from `AbstractBaseUser`. `groups` and `user_permissions` come from `PermissionsMixin`, and Django's `auth` app owns the Group and Permission tables.
- Deleting a user deletes the profile, and deleting the profile deletes its addresses (`CASCADE`).

## Planned: shop, cart, order, payment

This is a draft, and it will change as the models are written.

```mermaid
erDiagram
    USER ||--o| CART : owns
    USER ||--o{ ORDER : places

    CATEGORY |o--o{ CATEGORY : parent
    CATEGORY ||--o{ PRODUCT : contains
    BRAND ||--o{ PRODUCT : makes
    PRODUCT ||--o{ PRODUCT_IMAGE : has
    ATTRIBUTE ||--o{ ATTRIBUTE_VALUE : has
    PRODUCT }o--o{ ATTRIBUTE_VALUE : described_by

    CART ||--o{ CART_ITEM : holds
    PRODUCT ||--o{ CART_ITEM : in

    ORDER ||--o{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : ordered_as
    COUPON |o--o{ ORDER : applied_to
    ORDER ||--o{ PAYMENT : paid_by

    PRODUCT {
        bigint id PK
        string name
        string slug
        decimal price
        int stock
        decimal average_rating "stored for fast lists"
    }

    ORDER {
        bigint id PK
        bigint user_id FK
        decimal total
        decimal discount "stored apart from total"
        string status
        string shipping_recipient_name "copied from Address"
        string shipping_city "copied from Address"
    }
```

### Notes

- **Order does not link to Address.** It copies the shipping fields at checkout, so editing or deleting an address never changes an old order. This also supports guest checkout.
- The `USER` in this diagram is the same `account.User` as above.