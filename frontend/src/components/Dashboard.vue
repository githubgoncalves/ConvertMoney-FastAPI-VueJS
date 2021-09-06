<template>
  <div class="hello" style="text-align: center;">
    <Header />
    <div class="container mrgnbtm" >
          <div class="row">
            <div class="col-md-12">
                <Convert @convert="convertMoney($event)" />
            </div>
          </div>
    </div>
    <div class="row mrgnbtm">
        <TableMoney :tableMoney="tableMoney" />
    </div>
  </div>
</template>

<script>
import Header from './Header.vue'
import Convert from './Convert.vue'
import TableMoney from './TableMoney.vue'
import { convert } from '../services/ConvertService'

export default {
  name: 'Dashboard',
  components: {
    Header,
    Convert,
    TableMoney
  },
  data() {
      return {
          tableMoney: [],
          numberOfConvert: 0
      }
  },
  methods: {
    convertMoney(data) {
      console.log('data:::', data)
      convert(data).then(response => {
        console.log(response)
        this.tableMoney = response
        this.numberOfConvert = this.tableMoney.length
      })
    }
  },
  mounted () {

  }
}
</script>