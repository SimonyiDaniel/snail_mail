def hitelesites(email):

    # "hello.worldcom"    => An email address has to contain a '@' character!
    # "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
    # "@world.com"        => The username before the '@' character cannot be empty!
    # "hello@"            => The domain after the '@' character cannot be empty!
    # "hello@worldcom"    => An email address has to contain at least one '.' character!
    # "hell.o@worldcom"   => The domain has to contain at least one '.' character!
    # "he.llo@worldcom."  => The top-level domain cannot be empty!
    # "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
    # ".hello@world.com"  => The username cannot start with a '.' character!
    # "he.llo@.world.com" => The domain cannot start with a '.' character!
    # "hello@world.com"   => Valid email address :)


    length_of_email = len(email)
    number_of_at_characters = email.count("@")
    number_of_dot_characters = email.count(".")
    position_of_at = email.find("@")

    position_of_first_dot = email.find(".")
    position_of_last_dot = email.rfind(".")
    position_of_first_dot_after_the_at = email.find(".", position_of_at)


    error_message_no_at = "An email address has to contain a '@' character!"
    error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
    error_message_no_dot = "An email address has to contain at least one '.' character!"
    error_message_no_username = "The username before the '@' character cannot be empty!"
    error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
    error_message_no_server_name = "The domain cannot start with a '.' character!"
    error_message_no_tld = "The top-level domain cannot be empty!"
    error_message_short_tld = "The top-level domain has to be at least two characters long!"
    error_message_no_domain = "The domain after the '@' character cannot be empty!"
    error_message_invalid_username = "The username cannot start with a '.' character!"

    ok_message = "Valid email address :)"
    is_valid = True

        # 1. ha nincs benne @
    if '@' not in email:
        return error_message_no_at
       
        #2. ha tobb @ van benne mint 1
    if number_of_at_characters > 1:
        return error_message_too_many_at
   
    # Ketté választani az emailt
    username, domain = email.split('@')
    
        # 3. Ne legyen ures a username
    if not username:
        return error_message_no_username
    
        # 4. Ne legyen a domain ures
    if not domain:
        return error_message_no_domain
    
        # 5. Legyen minimum egy . benne
    if '.' not in email:
        return error_message_no_dot
    
        # 6. legyen minimum egy . a domainben
    if '.' not in domain:
        return error_message_no_dot_in_domain
    
        # 7. a mondatt ne vegzodjon .-ra szval a tld nem lesz ures
    if domain.endswith('.'):
        return error_message_no_tld
    
        # 8. a "tld" legyen minimum 2 karakter hosszu
    tld = domain.split('.')[-1]  #ezzel lesz "tld"
    
    if len(tld) < 2:
        return error_message_short_tld
    
    # 9. a nev ne kezdodjon ponttal
    if username.startswith('.'):
        return error_message_invalid_username
    
    # 10. a domain nem kezdodik ponttal
    if domain.startswith('.'):
        return error_message_no_server_name
    
    # 11. Iha mindenjo akkor legyen jo

    return "Valid email address :)"

email = input("Készen állsz megadni az email címed: ")
print(hitelesites(email))