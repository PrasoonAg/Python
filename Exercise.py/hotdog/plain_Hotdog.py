# Question:
#
# A hotdog shop wants to check whether a customer wants
# a plain hotdog or not.
#
# A plain hotdog means:
# - no ketchup
# - no mustard
# - no onion
#
# The function receives three boolean values:
#
# ketchup  -> True if ketchup is added
# mustard  -> True if mustard is added
# onion    -> True if onion is added
#
# Return True only if the hotdog has NO toppings.
# Otherwise return False.


def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """

    # NOT ketchup:
    # True only when ketchup is absent

    # NOT mustard:
    # True only when mustard is absent

    # NOT onion:
    # True only when onion is absent

    # AND means all three conditions must be true together

    return not ketchup and not mustard and not onion


# Examples

# No toppings
print(wants_plain_hotdog(False, False, False))
# Output: True


# Ketchup added
print(wants_plain_hotdog(True, False, False))
# Output: False


# Mustard added
print(wants_plain_hotdog(False, True, False))
# Output: False


# All toppings added
print(wants_plain_hotdog(True, True, True))
# Output: False