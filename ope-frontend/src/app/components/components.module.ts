import { PlatesComponent } from './plates/plates.component';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatInputModule } from '@angular/material/input';
import { MatMenuModule} from '@angular/material/menu';
import { SplashScreenComponent } from './splash-screen/splash-screen.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeMenuComponent } from './home-menu/home-menu.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MenuHeaderComponent } from './menu-header/menu-header.component';
import { OrderComponent } from './order/order.component';


@NgModule({
  declarations: [
    NavbarComponent,
    SplashScreenComponent,
    HomeMenuComponent,
    NotFoundComponent,
    LoginComponent,
    PlatesComponent,
    MenuHeaderComponent,
    OrderComponent,
    OrderComponent
  ],
  imports: [
    CommonModule,
    MatIconModule,
    MatProgressBarModule,
    MatButtonModule,
    MatSidenavModule,
    MatCardModule,
    MatButtonModule,
    MatInputModule,
    MatMenuModule,
    FormsModule,
    RouterModule,
    ReactiveFormsModule
  ],
  exports: [
    NavbarComponent,
    SplashScreenComponent,
    HomeMenuComponent,
    NotFoundComponent,
    LoginComponent,
    MenuHeaderComponent,
    OrderComponent,
    PlatesComponent
  ]
})
export class ComponentsModule { }
