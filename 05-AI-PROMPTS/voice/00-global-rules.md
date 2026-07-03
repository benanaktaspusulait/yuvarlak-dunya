# Pompom Hills - Global Voice Rules v2.1

## Kurallar

Her Pompom Hills sesi için bu kurallar geçerlidir:

- Orijinal karakter sesi yarat. Ünlü biri, gerçek çocuk, tanınmış aktör veya bilinen çizgi film karakteri taklit etme.
- Ses gerektiğinde çocuk gibi duyulabilir ama gerçek çocuk kaydı değil, güvenli stüdyo karakter performansı olarak yönlendirilmelidir.
- Teslimat yumuşak, sıcak, samimi ve okul öncesi güvenli olmalı.
- Varsayılan dil basit İngilizce'dir; senaryo istediği zaman Türkçe sloganlar kullanılabilir.
- Kelimeler 3-4 yaş çocuklar tarafından anlaşılabilecek kadar net olmalı.
- Bağırma, çığlık, alay, aşağılama, sert azarlama, panik, kötü adam tonu, korkunç fısıltı veya yoğun ağlama yok.
- Heyecan parlak ama kontrollü. Üzüntü kısa ve yumuşak olsun.
- Nefesler doğal ve sessiz olsun. Ağır nefes, dramatik duraklamalar veya yetişkin tiyatral yoğunluğu yok.
- Temiz stüdyo sesi, kuru veya hafif işlenmiş; müzik, reverb kuyruğu veya gürültülü arka plan yok.

## Voice Continuity

Bir karakterin sesi her sahnede aynı karakter sesi olarak kalmalıdır.

Her speaking shot için:

```text
For Shot 01, match the approved character Voice ID or voice reference.

For Shot 02+, match the previous speaking shot.

The speaking voice MUST remain identical throughout the entire episode.

Maintain:

- same voice identity
- same timbre
- same pitch
- same speaking speed
- same warmth
- same preschool energy
- same pronunciation
- same accent
- same age impression
- same emotional tone
- same recording quality

Never generate a different interpretation of the character voice.
Never replace the voice with a narrator.
Never make the character sound older or younger.

If multiple shots belong to the same episode, their voices must sound as if they were recorded during the same recording session.
```

Voice Reference veya Voice ID destekleyen sistemlerde aynı karakter için her shot'ta aynı Voice ID kullanılmalıdır.

Voice ID desteklenmiyorsa, onaylı karakter voice reference'ı yeniden kullanılmalı ve ses kayması QA'da işaretlenmelidir.

Önceki shot mevcutsa, önceki shot sesi aynı zamanda voice reference olarak kabul edilir.

## Ortak Negatif Ses Promptu

```text
No screaming, no shouting, no crying meltdown, no sarcasm, no villain voice, no scary whisper, no harsh adult tone, no mocking, no aggressive laughter, no realistic animal growls, no distorted voice, no robotic voice, no celebrity imitation, no known cartoon imitation, no rasp that sounds sick, no overacting, no fast talking, no dramatic trailer voice, no heavy reverb, no background music, no noisy room.
```

## Master Ses Yaratıcı Şablonu

```text
Create an original voice for [CHARACTER NAME] from Pompom Hills v2.1, a warm preschool 3D animated series for children aged 3-4.

Voice identity:
[AGE / TYPE / ROLE]

Tone:
[TONE DESCRIPTION]

Performance:
Soft, warm, sincere, emotionally clear, preschool-safe, easy to understand, no shouting, no sarcasm, no scary intensity.

Pace:
[WORDS PER MINUTE]

Pitch:
[PITCH RANGE OR RELATIVE RANGE]

Emotion range:
Happy, curious, gentle surprise, thinking, sleepy, brief soft sadness, playful warmth. Avoid anger, panic, teasing, and intense crying.

Use this catchphrase naturally:
"[CATCHPHRASE]"

Test lines:
1. "[LINE 1]"
2. "[LINE 2]"
3. "[LINE 3]"
```

## Quick Casting Matrix

| Character | Voice Size | Pace | Core Sound |
| --- | --- | --- | --- |
| Kiko | Medium-high child | 95-115 wpm | bright curious warmth |
| Mimi | High soft child | 85-105 wpm | airy rounded gentleness |
| Opa | Low-medium guide | 75-90 wpm | warm patient wisdom |
| Arda | Medium-high toddler boy | 100-115 wpm | bouncy playful energy |
| Noah | Medium-high boy | 100-115 wpm | funny creative sparkle |
| Aiko | Soft medium-high girl | 85-100 wpm | calm careful observation |
| Amara | Warm medium-high girl | 95-110 wpm | musical encouragement |
| Sofia | Medium-high girl | 95-110 wpm | expressive colour joy |
| Luca | Medium-high boy | 100-115 wpm | friendly adventure |
| Freya | Soft medium-high girl | 85-100 wpm | peaceful nature care |
| Tillo | Soft medium rabbit | 85-100 wpm | patient gardening warmth |
| Mirnik | High playful kitten | 95-110 wpm | soft comic mischief |
| Mimo | Medium-low turtle | 70-85 wpm | slow steady kindness |
