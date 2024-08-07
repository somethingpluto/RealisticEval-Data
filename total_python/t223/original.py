
# Function to simulate data
def simulate_data(num_records):
    data = []
    for _ in range(num_records):
        email = generate_email()
        validity = random.choice([0, 1])
        holder_name_match = random.choice([0, 1])
        domain = email.split('@')[1]
        domain_type = random.choice(['free', 'corporate', 'educational', 'unknown'])
        domain_quality = random.choice(['high', 'medium', 'low'])
        social_media_presence = random.choice([0, 1])
        data_breach_involvement = random.choice([0, 1])
        email_quality_score = random.randint(0, 100)

        data.append([email, validity, holder_name_match, domain, domain_type, domain_quality,
                     social_media_presence, data_breach_involvement, email_quality_score])

    return data