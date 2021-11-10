import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'b64'
})
export class B64Pipe implements PipeTransform {

  transform(base64img: string): string {
    return `data:image/png;base64, ${base64img}`;
  }

}
