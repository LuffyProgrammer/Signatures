using System.Security.Cryptography;


static T[] CombineTwoArrays<T>(T[] a1, T[] a2)
{
    T[] arrayCombined = new T[a1.Length + a2.Length];
    Array.Copy(a1, 0, arrayCombined, 0, a1.Length);
    Array.Copy(a2, 0, arrayCombined, a1.Length, a2.Length);
    return arrayCombined;
}


static byte[] StringToByteArray(string hex)
{
    return Enumerable.Range(0, hex.Length)
                     .Where(x => x % 2 == 0)
                     .Select(x => Convert.ToByte(hex.Substring(x, 2), 16))
                     .ToArray();
}

static string deviceId()
{
    string prefix = "42";
    string key = "02b258c63559d8804321c5d5065af320358d366f";

    Random rnd = new Random();
    byte[] identifier = new byte[20];
    rnd.NextBytes(identifier);
    HMACSHA1 hmac = new HMACSHA1(StringToByteArray(key));
    byte[] buffer = CombineTwoArrays(StringToByteArray(prefix), identifier);
    string result = BitConverter.ToString(hmac.ComputeHash(buffer)).Replace("-", "").ToLower();
    return prefix + BitConverter.ToString(identifier).Replace("-", "").ToLower() + result;
}


string device = deviceId();
Console.WriteLine(device);