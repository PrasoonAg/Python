# Question:
# A person wants to know whether they are prepared for today's weather.
#
# They are considered prepared if:
#
# 1. They have an umbrella
# OR
# 2. The rain is light (less than 5) AND they have a hood
# OR
# 3. It is NOT true that both:
#       - it is raining
#       - and it is a workday
#
# Write a Python program to check whether the person
# is prepared for the weather.


# Example situation
have_umbrella = False
rain_level = 8
have_hood = False
is_workday = False


# Final condition
prepared_for_weather = (
    
    # Condition 1:
    # If person has umbrella -> prepared
    have_umbrella

    # OR

    or (

        # Condition 2:
        # Rain should be less than 5
        # AND person should have hood

        (rain_level < 5) and have_hood
    )

    # OR

    or (

        # Condition 3:
        # First check:
        # Is it raining AND is it a workday?

        # rain_level > 0 -> checks if rain exists
        # is_workday -> checks if today is workday

        # If BOTH are true:
        #     True and True -> True
        #
        # Then NOT reverses it:
        #     not True -> False
        #
        # Meaning:
        # Person is NOT comfortable/prepared
        # because rain + work together is difficult

        not (rain_level > 0 and is_workday)
    )
)


# Print final result
print(prepared_for_weather)