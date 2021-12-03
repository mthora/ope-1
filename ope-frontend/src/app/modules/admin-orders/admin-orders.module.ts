import { ComponentsModule } from 'src/app/components/components.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InProgressComponent } from './in-progress/in-progress.component';
import { StatsComponent } from './stats/stats.component';



@NgModule({
  imports: [
    CommonModule,
    ComponentsModule
  ],
  declarations: [
    InProgressComponent,
    StatsComponent
  ]
})
export class AdminOrdersModule { }
