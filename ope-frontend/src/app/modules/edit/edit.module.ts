import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NewItemScreenComponent } from './new-item-screen/new-item-screen.component';
import { ComponentsModule } from 'src/app/components/components.module';
import { MatSidenavModule } from '@angular/material/sidenav';
import {MatToolbarModule} from '@angular/material/toolbar';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { NgxCurrencyModule } from "ngx-currency";

@NgModule({
  declarations: [
    NewItemScreenComponent
  ],
  imports: [
    CommonModule,
    ComponentsModule,
    MatSidenavModule,
    MatFormFieldModule,
    MatToolbarModule,
    MatSelectModule,
    MatInputModule,
    MatButtonModule,
    MatCheckboxModule,
    FormsModule,
    RouterModule,
    ReactiveFormsModule,
    NgxCurrencyModule
  ],
  exports: [
    NewItemScreenComponent
  ]
})
export class EditModule { }
