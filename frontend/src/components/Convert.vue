<template>
  <div class="container">
    <div class="row">
        <div class="col-md-12 mrgnbtm">
            <form>
                <div class="row">
                    <div class="form-group col-md-4">
                        <input type="text" class="form-control" v-model="from_" name="from" id="from" aria-describedby="from" placeholder="from" />
                    </div>
                    <div class="form-group col-md-4">
                        <input type="text" class="form-control" v-model="to_" name="to" id="to" placeholder="to" />
                    </div>
                     <div class="form-group col-md-3">
                        <input type="text" class="form-control" v-model="amount_" name="amount" id="amount" placeholder="amount" />
                    </div>
                    <div class="form-group col-md-1">
                        <button type="button" @click='convert()' class="btn btn-danger">Convert</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
    </div>
</template>

<script>
export default {
  name: 'Convert',
  data() {
    return {
      from_: '',
      to_: '',
      amount_: ''
    }
  },
  methods: {
      convert() {
          const payload = {
              from_: this.from_,
              to_: this.to_,
              amount_: this.amount_
          }
          this.$emit('convert', payload)
      },
      clearForm() {
          this.from_ = "";
          this.to_ = "";
          this.amount_ = "";
      }
  }
}
</script>