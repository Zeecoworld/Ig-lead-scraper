import urllib.parse

def generate_instagram_profile_search_url(search_terms, profile_type=None, include_terms=None, exclude_terms=None, exclude_phrases=None):
    base_url = "http://www.google.com/search?q="
    
    # Start with the site-specific search for Instagram
    query = "site:instagram.com"
    
    # Add default exclusions for Instagram
    default_exclusions = [
        "-inurl:(explore|directory|p|reel|stories|guide)",
        "-intitle:(posts|followers|following)"
    ]
    query += " " + " ".join(default_exclusions)
    
    # Add profile type specific filters
    if profile_type:
        if profile_type.lower() == 'personal':
            query += ' -intitle:"(official)" -intitle:"(verified)"'
        elif profile_type.lower() == 'business':
            query += ' (intitle:"(official)" OR intitle:"(verified)" OR intext:"email" OR intext:"contact")'
    
    # Add custom exclude phrases
    if exclude_phrases:
        if isinstance(exclude_phrases, str):
            exclude_phrases = [exclude_phrases]
        query += " " + " ".join(f'-"{phrase}"' for phrase in exclude_phrases)
    
    # Add search terms
    if isinstance(search_terms, str):
        search_terms = [search_terms]
    query += " +" + " +".join(f'"{term}"' for term in search_terms)
    
    # Add additional include terms
    if include_terms:
        if isinstance(include_terms, str):
            include_terms = [include_terms]
        query += " " + " ".join(f'+"{term}"' for term in include_terms)
    
    # Add exclude terms
    if exclude_terms:
        if isinstance(exclude_terms, str):
            exclude_terms = [exclude_terms]
        query += " " + " ".join(f'-"{term}"' for term in exclude_terms)
    
    # URL encode the query
    encoded_query = urllib.parse.quote(query)
    
    # Combine base URL and encoded query
    full_url = base_url + encoded_query
    
    return full_url

# Example usage
personal_url = generate_instagram_profile_search_url(
    "travel photographer",
    profile_type='personal',
    include_terms=["landscape", "wildlife"],
    exclude_phrases="Follow us",
    exclude_terms=["wedding", "portrait"]
)
print("Personal profile search URL:", personal_url)

business_url = generate_instagram_profile_search_url(
    "travel photographer",
    profile_type='business',
    include_terms=["professional", "booking"],
    exclude_phrases="DM for collab",
    exclude_terms=["student", "amateur"]
)
# print("Business profile search URL:", business_url)