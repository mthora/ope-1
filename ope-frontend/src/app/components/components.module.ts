import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatButtonModule } from '@angular/material/button';
import {MatSidenavModule} from '@angular/material/sidenav';
import { SplashScreenComponent } from './splash-screen/splash-screen.component';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeMenuComponent } from './home-menu/home-menu.component';


@NgModule({
  declarations: [
    NavbarComponent,
    SplashScreenComponent,
    HomeMenuComponent
  ],
  imports: [
    CommonModule,
    MatIconModule,
    MatProgressBarModule,
    MatButtonModule,
    MatSidenavModule,
    MatCardModule,
    MatButtonModule
  ],
  exports: [
    NavbarComponent,
    SplashScreenComponent,
    HomeMenuComponent
  ]
})
export class ComponentsModule { }
