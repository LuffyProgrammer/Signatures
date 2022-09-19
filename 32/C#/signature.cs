using System.Security.Cryptography;
using System.Text;

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

static string signature(string data)
{
    string prefix = "32";
    string key = "fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2";

    HMACSHA1 hmac = new HMACSHA1(StringToByteArray(key));
    byte[] buffer = Encoding.Default.GetBytes(data);
    byte[] result = hmac.ComputeHash(buffer);
    return Convert.ToBase64String(CombineTwoArrays(StringToByteArray(prefix), result));
}

string sig = signature("{}");
Console.WriteLine(sig);