import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'payment'
})
export class PaymentPipe implements PipeTransform {

  transform(value: number): string {
    let equivalent = '';
    switch (value.toString()) {
      case '1':
        equivalent = 'PIX';
        break
      case '2':
        equivalent = 'Crédito';
        break
      case '3':
        equivalent = 'Débito';
        break
      case '4':
        equivalent = 'Dinheiro';
        break
      default:
        equivalent = value.toString()
        break;
    }
    return equivalent
  }

}
