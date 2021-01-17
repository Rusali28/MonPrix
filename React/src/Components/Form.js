const Form = () => {
  return (
    <section className="section">
      <div className="container">
        <form>
          <label htmlFor="email">Email Address</label>
          <input id="email" name="email" type="email" />
          <button type="submit">Submit</button>
        </form>
      </div>
      {/* <Link to="/trade">Start now</Link> */}
    </section>
  );
};

export default Form;
