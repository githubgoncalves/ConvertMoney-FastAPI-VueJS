<template>
    <div class="container">
        <table class="table table-bordered">
            <thead>
            <tr>
                <th>FROM</th>
                <th>TO</th>
                <th>AMOUNT</th>
                <th>PRICE</th>
            </tr>
            </thead>
            <tbody>
              <tr>
                  <td>{{ tableMoney.from_ }}</td>
                  <td>{{ tableMoney.to_ }}</td>
                  <td>{{ tableMoney.amount_ }}</td>
                  <td>{{ tableMoney.price | currencydecimal}}</td>
              </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

    export default {
        name: 'TableMoney',
        props: ['tableMoney'],

        filters: {
            currencydecimal (value) {
                return value.toFixed(2)
            }
        }

     }
</script>