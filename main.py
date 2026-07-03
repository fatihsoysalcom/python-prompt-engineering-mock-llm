import textwrap

def mock_llm_response(prompt: str, input_text: str) -> str:
    """
    Simulates an LLM's response based on the prompt and input text.
    This function demonstrates the concept of prompt engineering without
    requiring an actual LLM API or external libraries, adhering to stdlib only.
    """
    prompt_lower = prompt.lower()

    if "özetle" in prompt_lower or "summarize" in prompt_lower:
        # This branch simulates a summarization task based on the prompt.
        # In a real LLM, the model would generate a concise summary.
        sentences = input_text.split('.')
        summary = ". ".join(sentences[:2]) + "." if len(sentences) > 1 else input_text
        return f"Özet:\n{textwrap.fill(summary.strip(), width=70)}"
    elif "anahtar kelimeleri çıkar" in prompt_lower or "extract keywords" in prompt_lower:
        # This branch simulates keyword extraction based on the prompt.
        # A real LLM would identify and list key terms.
        words = [word.lower() for word in input_text.replace('.', '').replace(',', '').split() if len(word) > 3]
        # Simple frequency-based keyword extraction for demonstration
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        sorted_keywords = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
        top_keywords = [word for word, count in sorted_keywords[:5]]
        return f"Anahtar Kelimeler: {', '.join(top_keywords)}"
    elif "fransızcaya çevir" in prompt_lower or "translate to french" in prompt_lower:
        # This branch simulates a translation task based on the prompt.
        # A real LLM would provide an accurate translation.
        return f"Fransızca Çeviri (Mock): 'Bonjour, {input_text[:30].strip()}...'"
    elif "duygu analizi yap" in prompt_lower or "sentiment analysis" in prompt_lower:
        # This branch simulates sentiment analysis based on the prompt.
        # A real LLM would determine the sentiment (positive, negative, neutral).
        if "harika" in input_text.lower() or "mükemmel" in input_text.lower() or "başarıydı" in input_text.lower():
            return "Duygu Analizi: Pozitif"
        elif "kötü" in input_text.lower() or "sorunlu" in input_text.lower():
            return "Duygu Analizi: Negatif"
        else:
            return "Duygu Analizi: Nötr"
    else:
        # This handles prompts the mock LLM doesn't understand, demonstrating prompt limitations.
        return f"Anlaşılamayan komut: '{prompt}'. Lütfen özetle, anahtar kelimeleri çıkar, Fransızcaya çevir veya duygu analizi yap gibi komutlar kullanın."

# Sample text to process, similar to content found in the article's context.
sample_text = """
Yapay zeka, özellikle büyük dil modelleri (LLM'ler) sayesinde, yazılım geliştirme süreçlerine devrim niteliğinde yenilikler getiriyor. Artık karmaşık algoritmaları ve iş mantığını binlerce satır kodla yazmak yerine, iyi tasarlanmış bir prompt ile bu görevleri LLM'lere devretmek mümkün. Bu, geliştirme süreçlerini hızlandırma, verimliliği artırma ve daha esnek çözümler üretme potansiyeli sunuyor.
"""

print("--- Prompt Mühendisliği Demostrasyonu (Mock LLM) ---")
print("Bu örnek, Python kodunu doğrudan yazmak yerine, bir 'prompt' (istem) kullanarak")
print("bir yapay zeka modelinden (burada simüle edilmiş) nasıl farklı çıktılar alınabileceğini gösterir.\n")

# --- Örnek 1: Metni Özetleme --- 
# Geleneksel olarak bu, metin işleme algoritmaları gerektirirdi. 
# Şimdi sadece bir prompt ile 'AI'dan özet istiyoruz. Bu, prompt mühendisliğinin gücüdür.
prompt_summary = "Yukarıdaki metni Türkçe olarak özetle."
print(f"Prompt: '{prompt_summary}'")
response_summary = mock_llm_response(prompt_summary, sample_text)
print(f"AI Yanıtı:\n{response_summary}\n")

# --- Örnek 2: Anahtar Kelime Çıkarma ---
# Geleneksel olarak bu, NLP kütüphaneleri ve karmaşık algoritmalar gerektirirdi.
# Prompt ile AI'dan anahtar kelimeleri çıkarmasını istiyoruz.
prompt_keywords = "Bu metinden en önemli anahtar kelimeleri çıkar."
print(f"Prompt: '{prompt_keywords}'")
response_keywords = mock_llm_response(prompt_keywords, sample_text)
print(f"AI Yanıtı:\n{response_keywords}\n")

# --- Örnek 3: Duygu Analizi ---
# Geleneksel olarak bu, makine öğrenimi modelleri ve eğitim verileri gerektirirdi.
# Prompt ile AI'dan metnin duygusunu analiz etmesini istiyoruz.
sentiment_text = "Bu proje harika bir başarıydı! Ekip mükemmel bir iş çıkardı."
prompt_sentiment = f"Aşağıdaki metnin duygu analizini yap: '{sentiment_text}'"
print(f"Prompt: '{prompt_sentiment}'")
response_sentiment = mock_llm_response(prompt_sentiment, sentiment_text)
print(f"AI Yanıtı:\n{response_sentiment}\n")

# --- Örnek 4: Farklı bir prompt ile aynı metin üzerinde ---
# Prompt'u değiştirerek farklı bir görev talep ediyoruz, bu da LLM'lerin esnekliğini gösterir.
prompt_french = "Yukarıdaki metnin ilk cümlesini Fransızcaya çevir."
print(f"Prompt: '{prompt_french}'")
response_french = mock_llm_response(prompt_french, sample_text.split('.')[0])
print(f"AI Yanıtı:\n{response_french}\n")

# --- Örnek 5: Anlaşılamayan bir prompt ---
# İyi tasarlanmamış veya desteklenmeyen bir prompt'un nasıl sonuçlandığını gösterir.
prompt_unknown = "Bana bir şiir yaz."
print(f"Prompt: '{prompt_unknown}'")
response_unknown = mock_llm_response(prompt_unknown, "Herhangi bir metin.")
print(f"AI Yanıtı:\n{response_unknown}\n")
