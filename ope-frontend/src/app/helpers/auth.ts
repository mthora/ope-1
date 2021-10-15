import { EncodeHelper } from "./encode";

export class JwtHelper {
    static decode(token: string): any {
        if (!token) {
            return null;
        }

        // Split the token
        const parts = token.split('.');

        if (parts.length !== 3) {
            throw new Error('Token inválido.');
        }

        // Decode the token using the Base64 decoder
        const decoded = EncodeHelper.FromBase64(parts[1]);

        if (!decoded) {
            throw new Error('Cannot decode the token.');
        }

        return JSON.parse(decoded);
    }

    static getExpirationDate(token: string): Date | null {
        const jwt = JwtHelper.decode(token);

        if (jwt && jwt.exp) {
            const date = new Date(0);
            date.setUTCSeconds(jwt.exp);

            return date;
        }

        return null;
    }
}
