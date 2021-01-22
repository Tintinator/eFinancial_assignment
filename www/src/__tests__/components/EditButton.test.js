import React from "react";
import { shallow, configure } from "enzyme";
import EditButton from "../../components/EditButton";
import Adapter from "@wojtekmaj/enzyme-adapter-react-17";

configure({ adapter: new Adapter() });
test("Button reflects isEdit prop", () => {
  const componentNoEdit = shallow(<EditButton isEdit={false} />);
  expect(componentNoEdit.text()).toEqual("Edit");

  const componentEdit = shallow(<EditButton isEdit={true} />);
  expect(componentEdit.text()).toEqual("Update");
});
