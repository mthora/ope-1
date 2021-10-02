import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SubMenuScreenComponent } from './sub-menu-screen/sub-menu-screen.component';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';



@NgModule({
  declarations: [
    SubMenuScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ]
})
export class MenuModule { }
