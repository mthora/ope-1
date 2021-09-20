import { ComponentsModule } from './../../components/components.module';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { HomeScreenComponent } from './home-screen/home-screen.component';
import { MatSidenavModule } from '@angular/material/sidenav';


@NgModule({
  declarations: [
    HomeScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ],
  exports: [
    HomeScreenComponent
  ]
})
export class HomeModule { }
