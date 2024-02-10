
const allwords = document.querySelectorAll('.clickableText');

allwords.forEach(wr => {
    wr.addEventListener('click', async (w) => {
    const word = w.target.innerHTML;
    console.log(word);

    const authKey = '7b13c975-fb53-4f67-938f-2f3d484a436e:fx';
    const endpoint = 'https://api-free.deepl.com/v2/translate';

    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
        'Authorization': 'DeepL-Auth-Key ${authKey}',
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        text: [word],
        target_lang: 'DE', // Change this to your desired target language code
        }),
    });

    const translation = await response.json();
    console.log(translation.translations[0].text);
    });
});


