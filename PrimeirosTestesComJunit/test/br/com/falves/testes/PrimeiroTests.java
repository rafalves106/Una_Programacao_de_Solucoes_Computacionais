/**
 * @author falvesmac
 */

package br.com.falves.testes;

import org.junit.Assert;
import org.junit.Test;

public class PrimeiroTests {
    @Test
    public void primeiroTeste() {
        String nome = "Rodrigo";
        Assert.assertEquals("Rodrigo", nome);
    }

    @Test
    public void testNotEquals() {
        String nome = "Rodrigo";
        Assert.assertNotEquals("Rodrigo1", nome);
    }

}