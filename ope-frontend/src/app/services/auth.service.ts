import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { environment } from 'src/environments/environment';
import { AuthUtils } from './auth.utils';
import jwt_decode from "jwt-decode";


@Injectable({
  providedIn: 'root',
})
export class AuthService {
    private _authenticated: boolean = false;
    private _urlAuth: string = `${environment.urlServer}users`;


    /**
     * Constructor
     */
    constructor(
        private _httpClient: HttpClient
    ) {}
  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  /**
   * Setter & getter for access token
   */
  set accessToken(token: string)
  {
    localStorage.setItem('authentication', token);
  }

  get accessToken(): string
  {
    const token = localStorage.getItem('authentication') || '';
    return token;
  }

   signIn(credentials: { email: string, senha: string }): Observable<any> {
        // Throw error, if the user is already logged in
        if (this.accessToken != "") {
            console.log("nope")
            return throwError('Usuário já logado!');
        }


        return this._httpClient.post(this._urlAuth + '/login', credentials).pipe(
            switchMap((response: any) => {
                // Store the user on the user service
                console.log(response);
                this.accessToken = response.data;

                // Return a new observable with the response
                return of(response);

            })
        );
    }
  /**
   * Sign in using the access token
   */
  signInUsingToken(): Observable<any>
  {

    // Renew token
    return this._httpClient.post('/login', {
      access_token: this.accessToken
    }).pipe(
      catchError(() => {

        // Return false
        return of(false);
      }),
      switchMap((response: any) => {

        // Store the access token in the local storage
        this.accessToken = response.access_token;

        // Set the authenticated flag to true
        this._authenticated = true;

        // Store the user on the user service
        this.accessToken = response.data;

        // Return true
        return of(true);
      })
    );
  }


  signOut(): Observable<any> {
    // Remove the access token from the local storage
    localStorage.removeItem('authentication');
    localStorage.clear();
    // Set the authenticated flag to false
    this._authenticated = false;

    // Return the observable
    return of(true);
  }

  /**
   * Check the authentication status
   */
  check(): Observable<boolean>
  {
    // Check if the user is logged in
    if ( this._authenticated )
    {
      return of(true);
    }

    // Check the access token availability
    if ( !this.accessToken )
    {
      return of(false);
    }

    // Check the access token expire date
    if ( AuthUtils.isTokenExpired(this.accessToken) )
    {
      return of(false);
    }

    // If the access token exists and it didn't expire, sign in using it
    return this.signInUsingToken();
  }

  getUserId(): any {
    console.log(this.accessToken);
    if (this.accessToken != ''){
      var decoded = jwt_decode(this.accessToken);
      console.log(decoded);
      return decoded;
    }
    return 0;
  }

}
