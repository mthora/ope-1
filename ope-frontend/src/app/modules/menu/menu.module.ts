import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SubMenuScreenComponent } from './sub-menu-screen/sub-menu-screen.component';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';
import { PlatesComponent } from 'src/app/components/plates/plates.component';
import { PlatesScreenComponent } from './plates-screen/plates-screen.component';



@NgModule({
  declarations: [
    SubMenuScreenComponent,
    PlatesScreenComponent
    
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule
  ]
})
export class MenuModule { }
