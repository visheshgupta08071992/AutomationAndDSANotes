# ChaiAssertion Cheat Sheet
## Chai

links: [chai home](http://chaijs.com/) , [docs](http://chaijs.com/api/)

#### Expect/Should (BDD)

links: [docs](http://chaijs.com/api/bdd/)

Chains:


   * to
   * be
    * been
    * is
    * that
    * which
    * and
    * has
    * have
    * with
    * at
    * of
    * same

<table>
    <thead>
        <tr>
            <th>Assertions</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
<tr>
	<td>.a(type)</td>
	<td>
        <p>
	        @param{ String }type<br/>
    	    @param{ String }message_optional_
        </p>
        <p>
            The a and an assertions are aliases that can be used either as language chains or to assert a value's type.
        </p>        
        <p>
            // typeof      
            <br/>
            <ul>
                <li> expect('test').to.be.a('string');</li>
                <li> expect({ foo: 'bar' }).to.be.an('object');</li>
                <li>expect(null).to.be.a('null');</li>
                <li>expect(undefined).to.be.an('undefined');</li>
            </ul>
        </p>
        <p>
            // language chain
            <ul>
                <li>expect(foo).to.be.an.instanceof(Foo);</li>
            </ul>
        </p>
    </td>
</tr>
<tr>
	<td>.above(value)</td>
	<td>
        <p>
	        @param{ Number }value<br/>
            @param{ String }message_optional_
        </p>
        <p>
            Asserts that the target is greater than value.
            <ul>
                <li>expect(10).to.be.above(5);</li>
            </ul>
        </p>
        <p>
            Can also be used in conjunction with length to assert a minimum length. The benefit being a more informative error message than if the length was supplied directly.
            <ul>
                <li>expect('foo').to.have.lengthOf.above(2);</li>
                <li>expect([ 1, 2, 3 ]).to.have.lengthOf.above(2);</li>
            </ul>
        </p> 
    </td>
</tr>
<tr>
		<td>.all</td>
		<td>Sets the all flag (opposite of the any flag) later used by the keys assertion.
<ul><li>expect(foo).to.have.all.keys('bar', 'baz');</li></ul>
</td>
	</tr>	

<tr>
		<td>.any</td>
		<td>Sets the any flag, (opposite of the all flag) later used in the keys assertion. 
		
<ul><li>expect(foo).to.have.any.keys('bar', 'baz');</li></ul>

</td>
	</tr>

<tr>
		<td>.arguments</td>
		<td>Asserts that the target is an arguments object.
<br/><br/>
function test () {<br/>
  expect(arguments).to.be.arguments;<br/>
}</td>
	</tr>

<tr>
	<td>.below(value)</td>
	<td>
        <p>
	        @param{ Number }value<br/>
            @param{ String }message_optional_
        </p>
        <p>
            Asserts that the target is less than value.
            <ul>
                <li> expect(5).to.be.below(10);</li>
            </ul>
        </p>
        <p>
            Can also be used in conjunction with length to assert a maximum length. The benefit being a more informative error message than if the length was supplied directly.
            <ul>
                <li>expect('foo').to.have.lengthOf.below(4);</li>
                <li>expect([ 1, 2, 3 ]).to.have.lengthOf.below(4);</li>
            </ul>
        </p>
    </td>
</tr>
<tr>
	<td>.change(function)</td>
	<td>
        <p>
	        @param{ String }object<br/>
            @param{ String }propertyname<br/>
            @param{ String }message_optional_<br/>
        </p>
        <p>
            Asserts that a function changes an object property
            <br/><br/>
            var obj = { val: 10 };
            <br/>
            var fn = function() { obj.val += 3 };
            <br/>
            var noChangeFn = function() { return 'foo' + 'bar'; };
            <ul>
                <li>expect(fn).to.change(obj, 'val');</li>
                <li>expect(noChangFn).to.not.change(obj, 'val')</li>
            </ul>
        </p>
    </td>
</tr>
	
<tr>
		<td>.closeTo(expected, delta)</td>
		<td>
    <p>
	@param{ Number }expected<br/>
    @param{ Number }delta<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target is equal expected, to within a +/- delta range.
</p>
<ul><li>expect(1.5).to.be.closeTo(1, 0.5);
</li></ul>

</td>
	</tr>
<tr>
		<td>.decrease(function)</td>
		<td>
<p>
    @param{ String }object<br/>
    @param{ String }propertyname<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that a function decreases an object property
</p>

var obj = { val: 10 };
<br/><br/>
var fn = function() { obj.val = 5 };
<ul><li>expect(fn).to.decrease(obj, 'val');
</li></ul>

</td>
	</tr>
<tr>
		<td>.deep</td>
		<td>Sets the deep flag, later used by the equal and property assertions.
	<br/>
<ul><li>expect(foo).to.deep.equal({ bar: 'baz' });</li>
<li>expect({ foo: { bar: { baz: 'quux' } } }).to.have.deep.property('foo.bar.baz', 'quux');</li></ul>

</td>
	</tr>
	<tr>
		<td>.empty</td>
		<td>Asserts that the target's length is 0. For arrays, it checks the length property. For objects, it gets the count of enumerable keys.
	<br/>
<ul><li>expect([]).to.be.empty;
</li><li>expect('').to.be.empty;</li>
<li>expect({}).to.be.empty;
</li></ul>
</td>
	</tr>
	
<tr>
	<td>.eql(value)</td>
	<td>
    	<p>
	        @param{ Mixed }value<br/>
   	        @param{ String }message_optional_
        </p>
        <p>
            Asserts that the target is deeply equal to value.
        </p>
        <ul>
            <li>expect([ 1, 2, 3 ]).to.eql([ 1, 2, 3 ]);</li>
            <li>expect({ foo: 'bar' }).to.eql({ foo: 'bar' });</li>
       </ul>
    </td>
</tr>

<tr>
	<td>.equal(value)</td>
	<td>
        <p>
	        @param{ Mixed }value<br/>
            @param{ String }message_optional_
        </p>
        <p>
            Asserts that the target is strictly equal (===) to value. Alternately, if the deep flag is set, asserts that the target is deeply equal to value.
        </p>
        <ul>
            <li>expect('hello').to.equal('hello');</li>
            <li>expect(42).to.equal(42);</li>
            <li>expect(1).to.not.equal(true);</li>
            <li>expect({ foo: 'bar' }).to.not.equal({ foo: 'bar' });</li>
            <li>expect({ foo: 'bar' }).to.deep.equal({ foo: 'bar' });</li>
        </ul>
    </td>
<tr>
	<td>.exist</td>
	<td>
	    Asserts that the target is neither null nor undefined.	       
        <p>
            var foo = 'hi',
                bar = null, 
                baz;        
        </p>    
                <br/><br/>        
        <ul>
            <li>expect(foo).to.exist;</li>
            <li>expect(bar).to.not.exist;</li>
            <li>expect(baz).to.not.exist;</li>
        </ul>
    </td>
</tr>


<tr>
    <td>.false</td>
    <td>
        Asserts that the target is false.
        <ul>
            <li>expect(false).to.be.false;</li>
            <li>expect(0).to.not.be.false;</li>
        </ul>         
    </td>
</tr>

<tr>
	<td>.include(value)</td>
	<td>
        <p>
	        @param{ Object | String | Number }obj<br/>
            @param{ String }message_optional_
        </p>
        <p>
            The include and contain assertions can be used as either property based language chains or as methods to assert the inclusion of an object in an array or a substring in a string. When used as language chains, they toggle the contains flag for the keys assertion.
        </p>
        <ul>
            <li>expect([1,2,3]).to.include(2);</li>
            <li>expect('foobar').to.contain('foo');</li>
            <li>expect({ foo: 'bar', hello: 'universe' }).to.include.keys('foo');</li>
        </ul>
	</td>
</tr>

<tr>
		<td>.increase(function)</td>
		<td>
    <p>
	@param{ String }object<br/>
    @param{ String }propertyname<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that a function increases an object property
</p>

var obj = { val: 10 };<br/>
var fn = function() { obj.val = 15 };</br>
<ul><li> expect(fn).to.increase(obj, 'val');</li></ul>

</td>
	</tr>
<tr>
		<td>.instanceof(constructor)</td>
		<td>
    <p>
	@param{ Constructor }constructor<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target is an instance of constructor.
</p>

var Tea = function (name) { this.name = name; }<br/>
  , Chai = new Tea('chai');

<ul><li>expect(Chai).to.be.an.instanceof(Tea);</li>
<li>expect([ 1, 2, 3 ]).to.be.instanceof(Array);</li></ul>

</td>
	</tr>
<tr>
		<td>.itself</td>
		<td>Sets the itself flag, later used by the respondTo assertion.
<br/>
function Foo() {}<br/>
Foo.bar = function() {}<br/>
Foo.prototype.baz = function() {}<br/>

<ul><li>expect(Foo).itself.to.respondTo('bar');</li>
<li>expect(Foo).itself.not.to.respondTo('baz');</li></ul>

</td>
	</tr>
<tr>
		<td>.keys(key1, [key2], [...])</td>
		<td>
<p>
    @param{ String... | Array | Object }keys
</p>
<p>
Asserts that the target contains any or all of the passed-in keys. Use in combination with any, all, contains, or have will affect what will pass.<br/>
When used in conjunction with any, at least one key that is passed in must exist in the target object. This is regardless whether or not the have or contain qualifiers are used. Note, either any or all should be used in the assertion. If neither are used, the assertion is defaulted to all.
<br/>
When both all and contain are used, the target object must have at least all of the passed-in keys but may have more keys not listed.
<br/>
When both all and have are used, the target object must both contain all of the passed-in keys AND the number of keys in the target object must match the number of keys passed in (in other words, a target object must have all and only all of the passed-in keys).
<br/>
</p>
<ul><li>expect({ foo: 1, bar: 2 }).to.have.any.keys('foo', 'baz');</li>
<li>expect({ foo: 1, bar: 2 }).to.have.any.keys('foo');</li>
<li>expect({ foo: 1, bar: 2 }).to.contain.any.keys('bar', 'baz');</li>
<li>expect({ foo: 1, bar: 2 }).to.contain.any.keys(['foo']);</li>
<li>expect({ foo: 1, bar: 2 }).to.contain.any.keys({'foo': 6});</li>
<li>expect({ foo: 1, bar: 2 }).to.have.all.keys(['bar', 'foo']);</li>
<li> expect({ foo: 1, bar: 2 }).to.have.all.keys({'bar': 6, 'foo': 7});</li>
<li>expect({ foo: 1, bar: 2, baz: 3 }).to.contain.all.keys(['bar', 'foo']);</li>
<li>expect({ foo: 1, bar: 2, baz: 3 }).to.contain.all.keys([{'bar': 6}}]);</li>
</ul>

</td>
	</tr>
<tr>
		<td>.least(value)</td>
		<td>
    <p>
	@param{ Number }value<br/>
    @param{ String }message_optional_
    </p>
<p>
    Asserts that the target is greater than or equal to value.

    <ul>
        <li>expect(10).to.be.at.least(10);</li>
    </ul>
</p>
</td>
	</tr>

<tr>
		<td>.lengthOf(value)</td>
		<td>

<p>
    @param{ Number }length<br/>
    @param{ String }message_optional_<br/><br/>
   
    Asserts that the target's length property has the expected value.
</p>

<ul>
<li>expect([ 1, 2, 3]).to.have.lengthOf(3);</li>
<li>expect('foobar').to.have.length(6);</li>
</ul>

<p>
Can also be used as a chain precursor to a value comparison for the length property.
</p>
<ul>
<li>expect('foo').to.have.lengthOf.above(2);</li>
<li>expect([ 1, 2, 3 ]).to.have.lengthOf.above(2);</li>
<li>expect('foo').to.have.lengthOf.below(4);</li>
<li>expect('foo').to.have.lengthOf.below(4);</li>
<li>expect([ 1, 2, 3 ]).to.have.lengthOf.below(4);</li>
<li>expect('foo').to.have.lengthOf.within(2,4);</li>
<li>expect([ 1, 2, 3 ]).to.have.lengthOf.within(2,4);</li>
</ul>

</td>
	</tr>

<tr>
		<td>.match(regexp)</td>
		<td>
<p>
    @param{ RegExp }RegularExpression<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target matches a regular expression.
</p>

<ul><li>expect('foobar').to.match(/^foo/);</li></ul>

</td>
	</tr>

<tr>
		<td>.members(set)</td>
		<td>
    <p>
	@param{ Array }set<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target is a superset of set, or that the target and set have the same strictly-equal (===) members. Alternately, if the deep flag is set, set members are compared for deep equality.
</p>
<ul><li>expect([1, 2, 3]).to.include.members([3, 2]);</li>
<li>expect([1, 2, 3]).to.not.include.members([3, 2, 8]);</li>
<li>expect([4, 2]).to.have.members([2, 4]);</li>
<li>expect([5, 2]).to.not.have.members([5, 2, 1]);</li>
<li>expect([{ id: 1 }]).to.deep.include.members([{ id: 1 }]);</li></ul>

</td>
	</tr>
<tr>
		<td>.most(value)</td>
		<td>
    
<p>
	@param{ Number }value<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target is less than or equal to value.
</p>

<ul><li> expect(5).to.be.at.most(5);</li></ul>

<p>
Can also be used in conjunction with length to assert a maximum length. The benefit being a more informative error message than if the length was supplied directly.
</p>

<ul><li>expect('foo').to.have.lengthOf.at.most(4);</li>
<li> expect([ 1, 2, 3 ]).to.have.lengthOf.at.most(3);</li></ul>

</td>
	</tr>
 <tr>
            <td>.not</td>
		<td>Negates any of assertions following in the chain.

<ul><li>expect(foo).to.not.equal('bar');</li>
<li>expect(goodFn).to.not.throw(Error);</li><li>expect({ foo: 'baz' }).to.have.property('foo').and.not.equal('bar');</li></ul>

</td>
        </tr>

<tr>
		<td>.null</td>
		<td>Asserts that the target is null.
<br/>
<ul><li>expect(null).to.be.null;</li>
<li>expect(undefined).not.to.be.null;</li></ul>

</td>
	</tr>


<tr> 
		<td>.ok</td>
		<td>Asserts that the target is truthy.</td>
	</tr>

<tr>
		<td>.ownProperty(name)</td>
		<td>
<p>
    @param{ String }name<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target has an own property name.
</p>

<ul><li> expect('test').to.have.ownProperty('length');</li></ul>

</td>
	</tr>
	
<tr>
		<td>.property(name, [value])</td>
		<td>
<p>
    @param{ String }name<br/>
    @param{ Mixed }value(optional)<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target has a property name, optionally asserting that the value of that property is strictly equal to value. If the deep flag is set, you can use dot- and bracket-notation for deep references into objects and arrays.
</p>

// simple referencing<br/>
var obj = { foo: 'bar' };<br/>

<ul><li>expect(obj).to.have.property('foo');</li><li>expect(obj).to.have.property('foo', 'bar');</li></ul>
<br/>
// deep referencing<br/>

var deepObj = {<br/>
    green: { tea: 'matcha' }<br/>
  , teas: [ 'chai', 'matcha', { tea: 'konacha' } ]<br/>
};<br/>

<ul>
<li>expect(deepObj).to.have.deep.property('green.tea', 'matcha');</li>
<li>expect(deepObj).to.have.deep.property('teas[1]', 'matcha');</li>
<li>expect(deepObj).to.have.deep.property('teas[2].tea', 'konacha');</li>
</ul>

<p>You can also use an array as the starting point of a deep.property assertion, or traverse nested arrays.</p>

var arr = [<br/>
    [ 'chai', 'matcha', 'konacha' ]<br/>
  , [ { tea: 'chai' }<br/>
    , { tea: 'matcha' }<br/>
    , { tea: 'konacha' } ]<br/>
];<br/>

<ul>
<li>expect(arr).to.have.deep.property('[0][1]', 'matcha');</li>
<li>expect(arr).to.have.deep.property('[1][2].tea', 'konacha');</li>
</ul>

<p>
Furthermore, property changes the subject of the assertion to be the value of that property from the original object. This permits for further chainable assertions on that property.
</p>

<ul><li>expect(obj).to.have.property('foo').that.is.a('string');</li>
<li>expect(deepObj).to.have.property('green').that.is.an('object').that.deep.equals({ tea: 'matcha' });</li>
<li>expect(deepObj).to.have.property('teas').that.is.an('array').with.deep.property('[2]').that.deep.equals({ tea: 'konacha' });</li></ul>

</td>
	</tr>

<tr>
		<td>.respondTo(method)</td>
		<td>
<p>
    @param{ String }method<br/>
    @param{ String }message_optional_
</p>

<p>
Asserts that the object or class target will respond to a method.
</p>
Klass.prototype.bar = function(){};<br/>

<ul><li>expect(Klass).to.respondTo('bar');</li>
<li>expect(obj).to.respondTo('bar');</li></ul>

<p>
To check if a constructor will respond to a static function, set the itself flag.
</p>

Klass.baz = function(){};<br/>

<ul><li>expect(Klass).itself.to.respondTo('baz');</li></ul>

</td>
	</tr>
<tr>
		<td>.satisfy(method)</td>
		<td>
    <p>
	@param{ Function }matcher<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the target passes a given truth test.
</p>

<ul><li>expect(1).to.satisfy(function(num) { return num > 0; });</li></ul>

</td>
	</tr>
<tr>
		<td>.string(string)</td>
		<td>
<p>
    @param{ String }string<br/>
    @param{ String }message_optional_
</p>
<p>
Asserts that the string target contains another string.
</p>
<ul><li>expect('foobar').to.have.string('bar');</li></ul>


</td>
	</tr>

<tr>
		<td>.throw(constructor)</td>
		<td>
<p>    
	@param{ ErrorConstructor }constructor<br/>
    @param{ String | RegExp }expectederror message<br/>
    @param{ String }message_optional_<br/>
    @see: [https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Error#Error_types]()
</p>
Asserts that the function target will throw a specific error, or specific type of error (as determined using instanceof), optionally with a RegExp or string inclusion test for the error's message.
<br/><br/>
var err = new ReferenceError('This is a bad function.');
<br/></br>
var fn = function () { throw err; }
<br/>
<ul>
<li>expect(fn).to.throw(ReferenceError);</li>
<li> expect(fn).to.throw(Error);</li>
<li>expect(fn).to.throw(/bad function/);</li>
<li>expect(fn).to.not.throw('good function');</li>
<li>expect(fn).to.throw(ReferenceError, /bad function/);</li>
<li>expect(fn).to.throw(err);</li>
<li>expect(fn).to.not.throw(new RangeError('Out of range.'));</li>
</ul>
Please note that when a throw expectation is negated, it will check each parameter independently, starting with error constructor type. The appropriate way to check for the existence of a type of error but for a message that does not match is to use and.

<ul>
<li>expect(fn).to.throw(ReferenceError)
   .and.not.throw(/good function/);
</li>
</ul>
</td>
	</tr>
<tr>
		<td>.true</td>
		<td>Asserts that the target is true.

<ul><li>expect(true).to.be.true;</li>
<li>expect(1).to.not.be.true;</li></ul>

</td>
	</tr>
<tr>
		<td>.undefined</td>
		<td>Asserts that the target is undefined.

<ul><li>expect(undefined).to.be.undefined;</li>
<li>expect(null).to.not.be.undefined;</li></ul>

</td>
	</tr>
	
<tr>
		<td>.within(start, finish)</td>
		<td>
    <p>
	@param{ Number }startlowerbound inclusive<br/>
    @param{ Number }finishupperbound inclusive<br/>
    @param{ String }message_optional_
</p>
Asserts that the target is within a range.

<ul><li> expect(7).to.be.within(5,10);</li></ul>
<br/>

Can also be used in conjunction with length to assert a length range. The benefit being a more informative error message than if the length was supplied directly.

<ul><li>expect('foo').to.have.lengthOf.within(2,4);</li>
<li>expect([ 1, 2, 3 ]).to.have.lengthOf.within(2,4);</li></ul>

</td>
	</tr>
</tbody>
</table>
