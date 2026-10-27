# Apps and their responsibilities

## account
Owns: custom User, Profile, Address, registration, login, logout,
activation, password recovery, profile edit.
Does not own: orders or payments.

## shop
Owns: Category, Brand, Product, Attribute, product images, search,
filtering, ordering, latest and similar products.

## cart
Owns: Cart and CartItem, the session cart for anonymous users,
merging it into the database cart on login.

## order
Owns: Order, OrderItem, Coupon, coupon validation.
Stores a copy of price and address at order time.

## payment
Owns: Payment models, the gateway integration (Zarinpal), callbacks.

## Planned
wishlist, reviews, newsletter, contact us