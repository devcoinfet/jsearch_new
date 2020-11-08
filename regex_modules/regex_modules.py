
REGEX_PATT = {
    #"AMAZON_URL":r"https?://[^\"\\'> ]+",
    "AMAZON_URL_1":r"[a-z0-9.-]+\.s3-[a-z0-9-]\\.amazonaws\.com",
    "AMAZON_URL_2":r"[a-z0-9.-]+\.s3-website[.-](eu|ap|us|ca|sa|cn)",
    "AMAZON_URL_3":r"s3\\.amazonaws\.com/[a-z0-9._-]+",
    "AMAZON_URL_4":r"s3-[a-z0-9-]+\.amazonaws\\.com/[a-z0-9._-]+",
    "URLS":r"http?://[^\"\\'> ]+",
    "AMAZON_KEY":r"([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}",
    "Authorization":r"^Bearer\s[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
    "accessToken":r"^acesstoken=[0-9]{13,17}",
    "vtex-key":r"vtex-api-(appkey|apptoken)",
    "api-key":r"api-key-(api_key|apikey)",
    "uploads":r"uploads-(upload|uploader)",
    "admin":r"admin",
    "email":r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
    "IP_Address":r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
    
}
