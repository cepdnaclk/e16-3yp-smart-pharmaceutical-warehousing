#include <avr/io.h>
#include <util/delay.h>
#include <stdlib.h>
#include <stdio.h>

#define F_CPU  16000000UL

// CALATE 9600 BAUD RATE PRESCALER
#define BAUD_PRESCALE (((F_CPU / (9600 * 16UL))) - 1)

void usart_init()
{
    // SETUP BAUD RATE
    UBRR0H = BAUD_PRESCALE >> 8 ;
    UBRR0L = BAUD_PRESCALE ;

    // RX , TX SETUP
    UCSR0B = ( 1 << RXEN0 ) | ( 1 << TXEN0);

    // SET 8 BIT
    UCSR0C |=  (3<<UCSZ00) ;

    // NO PARITY DISABLE
    UCSR0C |= (0<<UPM00);

    // STOP BIT 1
    UCSR0C |= (0<<USBS0);


}

void usart_send( uint8_t DataByte ){

    while (( UCSR0A & (1<<UDRE0)) == 0) ; // wait untile free
    UDR0 = DataByte;

}

uint8_t usart_receive(){

    uint8_t DataByte ;
    while (( UCSR0A & (1<<RXC0)) == 0) ; // waite untile free

    DataByte = UDR0 ;
    return DataByte;

}



int main(){

    usart_init();
    while (1)
    {
        usart_send('A');
        usart_send('R');

        _delay_ms(1000);
    }
    return 0;

}