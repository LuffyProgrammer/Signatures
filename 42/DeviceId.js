const crypto = require('crypto')

function generate_device_id() {
    let identifier = crypto.randomBytes(20)
    let key = bytesToHex("02b258c63559d8804321c5d5065af320358d366f")
    var mac = crypto.createHmac("sha1", key)
    .update("\x42"+identifier)
    .digest('hex')

    return `42${identifier.toString('hex')}${mac}`
}

function bytesToHex(bytes) {
    for (var hex = [], i = 0; i < bytes.length; i++) {
        var current = bytes[i] < 0 ? bytes[i] + 256 : bytes[i];
        hex.push((current >>> 4).toString(16));
        hex.push((current & 0xF).toString(16));
    }
    return hex.join("");
}

console.log(generate_device_id());
