package Generators;

import org.apache.commons.codec.digest.HmacUtils;
import java.util.Arrays;
import java.util.Base64;

public class NdcMsgSigGen {
    private static byte[] hexStringToByteArray(String s) {
        int len = s.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i+1), 16));
        }
        return data;
    }

    private static byte[] concat(byte[] a, byte[] b) {
        int lenA = a.length;
        int lenB = b.length;
        byte[] c = Arrays.copyOf(a, lenA + lenB);
        System.arraycopy(b, 0, c, lenA, lenB);
        return c;
    }

    public static void main(String[] args) {
        String data = "{}";

        byte[] hmac = HmacUtils.hmacSha1(hexStringToByteArray("fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2"), data.getBytes());
        String finall = Base64.getEncoder().encodeToString(concat(hexStringToByteArray("32"), hmac));

        System.out.println(finall);
    }
}

