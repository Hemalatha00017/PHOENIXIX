import psycopg2
import os

def update_lead_status(phone, intent, score):
    conn = psycopg2.connect(os.getenv("POSTGRES_URL"))
    cur = conn.cursor()

    cur.execute("""
        UPDATE leads
        SET intent = %s,
            hot_score = %s,
            status = %s
        WHERE phone_number = %s
    """, (
        intent,
        score,
        "HOT" if score >= 70 else "COLD",
        phone
    ))

    conn.commit()
    cur.close()
    conn.close()
