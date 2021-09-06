

export async function convert(data) {
  const response = await fetch("http://localhost:5000/api/convert-currency?from_="+data.from_+"&to_="+data.to_+"&amount_="+data.amount_);
  return await response.json();
}